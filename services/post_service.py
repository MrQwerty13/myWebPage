from __future__ import annotations

from models.post import Post
from storage import posts_store


class PostError(Exception):
    pass


class PostService:
    def create_post(self, author_id: str, drink_name: str, content: str) -> Post:
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

        post = Post.create(author_id=author_id, drink_name=drink_name, content=content)
        posts_store.append(post.to_dict())
        return post

    def get_by_id(self, post_id: str) -> Post | None:
        raw = posts_store.find(lambda p: p["id"] == post_id)
        return Post.from_dict(raw) if raw else None

    def list_recent(self, limit: int = 30) -> list[Post]:
        raw_posts = posts_store.all()
        raw_posts.sort(key=lambda p: p.get("created_at", ""), reverse=True)
        return [Post.from_dict(raw) for raw in raw_posts[:limit]]

    def delete_post(self, post_id: str) -> bool:
        removed = posts_store.delete_where(lambda p: p["id"] == post_id)
        return removed > 0
