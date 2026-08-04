from __future__ import annotations

from models.like import Like
from storage import connect


class LikeService:
    def stats_for_feed(
        self,
        post_ids: set[str],
        user_id: str | None,
    ) -> tuple[dict[str, int], set[str]]:
        """Counts for given posts + which ones the user liked."""
        counts: dict[str, int] = {}
        liked_ids: set[str] = set()
        if not post_ids:
            return counts, liked_ids

        placeholders = ",".join("?" for _ in post_ids)
        params = tuple(post_ids)
        with connect() as conn:
            rows = conn.execute(
                f"""
                SELECT post_id, COUNT(*) AS cnt
                FROM likes
                WHERE post_id IN ({placeholders})
                GROUP BY post_id
                """,
                params,
            ).fetchall()
            for row in rows:
                counts[row["post_id"]] = row["cnt"]

            if user_id:
                liked_rows = conn.execute(
                    f"""
                    SELECT post_id FROM likes
                    WHERE user_id = ? AND post_id IN ({placeholders})
                    """,
                    (user_id, *params),
                ).fetchall()
                liked_ids = {row["post_id"] for row in liked_rows}

        return counts, liked_ids

    def toggle_like(self, post_id: str, user_id: str) -> dict:
        with connect() as conn:
            existing = conn.execute(
                "SELECT id FROM likes WHERE post_id = ? AND user_id = ?",
                (post_id, user_id),
            ).fetchone()

            if existing:
                conn.execute("DELETE FROM likes WHERE id = ?", (existing["id"],))
                liked = False
            else:
                like = Like.create(post_id=post_id, user_id=user_id)
                conn.execute(
                    """
                    INSERT INTO likes (id, post_id, user_id, created_at)
                    VALUES (?, ?, ?, ?)
                    """,
                    (like.id, like.post_id, like.user_id, like.created_at),
                )
                liked = True

            like_count = conn.execute(
                "SELECT COUNT(*) FROM likes WHERE post_id = ?",
                (post_id,),
            ).fetchone()[0]

        return {"liked": liked, "like_count": like_count}

    def delete_for_post(self, post_id: str) -> int:
        with connect() as conn:
            cur = conn.execute("DELETE FROM likes WHERE post_id = ?", (post_id,))
            return cur.rowcount
