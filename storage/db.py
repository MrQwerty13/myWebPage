from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "aftertaste.db"

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY,
    author_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    drink_name TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS likes (
    id TEXT PRIMARY KEY,
    post_id TEXT NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL,
    UNIQUE(post_id, user_id)
);

CREATE TABLE IF NOT EXISTS comments (
    id TEXT PRIMARY KEY,
    post_id TEXT NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    author_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_posts_created ON posts(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_likes_post ON likes(post_id);
CREATE INDEX IF NOT EXISTS idx_comments_post ON comments(post_id, created_at);
"""


def init_db() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript(SCHEMA)
        _migrate_json_if_needed(conn)


@contextmanager
def connect() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def _load_json_array(path: Path) -> list:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data if isinstance(data, list) else []


def _migrate_json_if_needed(conn: sqlite3.Connection) -> None:
    """One-shot import from legacy JSON files when the DB is empty."""
    user_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if user_count:
        return

    users = _load_json_array(DATA_DIR / "users.json")
    posts = _load_json_array(DATA_DIR / "posts.json")
    likes = _load_json_array(DATA_DIR / "likes.json")
    if not users and not posts and not likes:
        return

    for row in users:
        conn.execute(
            """
            INSERT OR IGNORE INTO users (id, username, email, password_hash, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                row["id"],
                row["username"],
                row["email"],
                row["password_hash"],
                row["created_at"],
            ),
        )

    user_ids = {
        row[0] for row in conn.execute("SELECT id FROM users").fetchall()
    }

    for row in posts:
        if row.get("author_id") not in user_ids:
            continue
        conn.execute(
            """
            INSERT OR IGNORE INTO posts
                (id, author_id, drink_name, content, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, NULL)
            """,
            (
                row["id"],
                row["author_id"],
                row["drink_name"],
                row["content"],
                row["created_at"],
            ),
        )

    post_ids = {
        row[0] for row in conn.execute("SELECT id FROM posts").fetchall()
    }

    for row in likes:
        if row.get("post_id") not in post_ids or row.get("user_id") not in user_ids:
            continue
        conn.execute(
            """
            INSERT OR IGNORE INTO likes (id, post_id, user_id, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (row["id"], row["post_id"], row["user_id"], row["created_at"]),
        )
