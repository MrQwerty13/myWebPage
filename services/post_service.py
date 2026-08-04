from __future__ import annotations

from models.post import Post
from models.user import utc_now_iso
from storage import connect


class PostError(Exception):
    pass


class PostService:
    def create_post(self, author_id: str, drink_name: str, content: str) -> Post:
        drink_name, content = self._validate(drink_name, content)
        post = Post.create(author_id=author_id, drink_name=drink_name, content=content)
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO posts
                    (id, author_id, drink_name, content, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, NULL)
                """,
                (
                    post.id,
                    post.author_id,
                    post.drink_name,
                    post.content,
                    post.created_at,
                ),
            )
        return post

    def update_post(
        self,
        post_id: str,
        author_id: str,
        drink_name: str,
        content: str,
    ) -> Post:
        drink_name, content = self._validate(drink_name, content)
        with connect() as conn:
            row = conn.execute(
                "SELECT * FROM posts WHERE id = ?",
                (post_id,),
            ).fetchone()
            if not row:
                raise PostError("post_missing")
            if row["author_id"] != author_id:
                raise PostError("post_forbidden")

            updated_at = utc_now_iso()
            conn.execute(
                """
                UPDATE posts
                SET drink_name = ?, content = ?, updated_at = ?
                WHERE id = ?
                """,
                (drink_name, content, updated_at, post_id),
            )
            return Post(
                id=post_id,
                author_id=author_id,
                drink_name=drink_name,
                content=content,
                created_at=row["created_at"],
                updated_at=updated_at,
            )

    def get_by_id(self, post_id: str) -> Post | None:
        with connect() as conn:
            row = conn.execute(
                "SELECT * FROM posts WHERE id = ?",
                (post_id,),
            ).fetchone()
        return Post.from_row(row) if row else None

    def list_recent(self, limit: int = 30) -> list[Post]:
        with connect() as conn:
            rows = conn.execute(
                """
                SELECT * FROM posts
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return [Post.from_row(row) for row in rows]

    def delete_post(self, post_id: str, author_id: str | None = None) -> bool:
        """Delete a post. If author_id is set, only that author may delete."""
        with connect() as conn:
            row = conn.execute(
                "SELECT author_id FROM posts WHERE id = ?",
                (post_id,),
            ).fetchone()
            if not row:
                return False
            if author_id is not None and row["author_id"] != author_id:
                raise PostError("post_forbidden")
            conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
            return True

    @staticmethod
    def _validate(drink_name: str, content: str) -> tuple[str, str]:
        drink_name = drink_name.strip()
        content = content.strip()

        if len(drink_name) < 1:
            raise PostError("drink_name_required")
        if len(drink_name) > 80:
            raise PostError("drink_name_too_long")
        if len(content) < 10:
            raise PostError("content_too_short")
        if len(content) > 2000:
            raise PostError("content_too_long")
        return drink_name, content
