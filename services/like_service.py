from __future__ import annotations

from collections import Counter

from models.like import Like
from storage import likes_store


class LikeService:
    def count_by_post(self) -> dict[str, int]:
        counts: Counter[str] = Counter()
        for raw in likes_store.all():
            counts[raw["post_id"]] += 1
        return dict(counts)

    def liked_post_ids_for_user(self, user_id: str) -> set[str]:
        return {
            raw["post_id"]
            for raw in likes_store.filter(lambda like: like["user_id"] == user_id)
        }

    def count_for_post(self, post_id: str) -> int:
        return len(likes_store.filter(lambda like: like["post_id"] == post_id))

    def user_liked_post(self, post_id: str, user_id: str) -> bool:
        return (
            likes_store.find(
                lambda like: like["post_id"] == post_id and like["user_id"] == user_id
            )
            is not None
        )

    def toggle_like(self, post_id: str, user_id: str) -> dict:
        existing = likes_store.find(
            lambda like: like["post_id"] == post_id and like["user_id"] == user_id
        )
        if existing:
            likes_store.delete_where(lambda like: like["id"] == existing["id"])
            liked = False
        else:
            like = Like.create(post_id=post_id, user_id=user_id)
            likes_store.append(like.to_dict())
            liked = True

        return {
            "liked": liked,
            "like_count": self.count_for_post(post_id),
        }
