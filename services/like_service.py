from __future__ import annotations

from models.like import Like
from storage import likes_store


class LikeService:
    def stats_for_feed(
        self,
        post_ids: set[str],
        user_id: str | None,
    ) -> tuple[dict[str, int], set[str]]:
        """One likes-file read: counts for given posts + which ones the user liked."""
        counts: dict[str, int] = {}
        liked_ids: set[str] = set()
        if not post_ids:
            return counts, liked_ids

        for raw in likes_store.all():
            post_id = raw["post_id"]
            if post_id not in post_ids:
                continue
            counts[post_id] = counts.get(post_id, 0) + 1
            if user_id and raw["user_id"] == user_id:
                liked_ids.add(post_id)
        return counts, liked_ids

    def toggle_like(self, post_id: str, user_id: str) -> dict:
        def mutate(items: list) -> dict:
            existing_index = None
            like_count = 0
            for index, item in enumerate(items):
                if item["post_id"] != post_id:
                    continue
                like_count += 1
                if item["user_id"] == user_id:
                    existing_index = index

            if existing_index is not None:
                items.pop(existing_index)
                liked = False
                like_count -= 1
            else:
                items.append(Like.create(post_id=post_id, user_id=user_id).to_dict())
                liked = True
                like_count += 1

            return {"liked": liked, "like_count": like_count}

        return likes_store.update(mutate)

    def delete_for_post(self, post_id: str) -> int:
        return likes_store.delete_where(lambda like: like["post_id"] == post_id)
