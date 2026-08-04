from __future__ import annotations

from models.comment import Comment
from storage import connect


class CommentError(Exception):
    pass


class CommentService:
    def create_comment(self, post_id: str, author_id: str, content: str) -> Comment:
        content = content.strip()
        if len(content) < 1:
            raise CommentError("comment_empty")
        if len(content) > 1000:
            raise CommentError("comment_too_long")

        with connect() as conn:
            post = conn.execute(
                "SELECT id FROM posts WHERE id = ?",
                (post_id,),
            ).fetchone()
            if not post:
                raise CommentError("post_missing")

            comment = Comment.create(
                post_id=post_id,
                author_id=author_id,
                content=content,
            )
            conn.execute(
                """
                INSERT INTO comments (id, post_id, author_id, content, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    comment.id,
                    comment.post_id,
                    comment.author_id,
                    comment.content,
                    comment.created_at,
                ),
            )
            return comment

    def list_for_post(self, post_id: str) -> list[Comment]:
        with connect() as conn:
            rows = conn.execute(
                """
                SELECT * FROM comments
                WHERE post_id = ?
                ORDER BY created_at ASC
                """,
                (post_id,),
            ).fetchall()
        return [Comment.from_row(row) for row in rows]

    def counts_for_posts(self, post_ids: set[str]) -> dict[str, int]:
        if not post_ids:
            return {}
        placeholders = ",".join("?" for _ in post_ids)
        with connect() as conn:
            rows = conn.execute(
                f"""
                SELECT post_id, COUNT(*) AS cnt
                FROM comments
                WHERE post_id IN ({placeholders})
                GROUP BY post_id
                """,
                tuple(post_ids),
            ).fetchall()
        return {row["post_id"]: row["cnt"] for row in rows}

    def delete_comment(self, comment_id: str, author_id: str | None = None) -> bool:
        with connect() as conn:
            row = conn.execute(
                "SELECT author_id FROM comments WHERE id = ?",
                (comment_id,),
            ).fetchone()
            if not row:
                return False
            if author_id is not None and row["author_id"] != author_id:
                raise CommentError("comment_forbidden")
            conn.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
            return True
