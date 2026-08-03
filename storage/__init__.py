from pathlib import Path

from storage.json_store import JsonStore

DATA_DIR = Path(__file__).resolve().parent / "data"

users_store = JsonStore(DATA_DIR / "users.json")
posts_store = JsonStore(DATA_DIR / "posts.json")
likes_store = JsonStore(DATA_DIR / "likes.json")
