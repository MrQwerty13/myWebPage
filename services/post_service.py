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
            raise PostError("Drink name is required.")
        if len(drink_name) > 80:
            raise PostError("Drink name is too long.")
        if len(content) < 10:
            raise PostError("Write at least 10 characters about the drink.")
        if len(content) > 2000:
            raise PostError("Opinion is too long (max 2000 characters).")

        post = Post.create(author_id=author_id, drink_name=drink_name, content=content)
        posts_store.append(post.to_dict())
        return post

    def get_by_id(self, post_id: str) -> Post | None:
        raw = posts_store.find(lambda p: p["id"] == post_id)
        return Post.from_dict(raw) if raw else None

    def list_recent(self, limit: int = 50) -> list[Post]:
        posts = [Post.from_dict(raw) for raw in posts_store.all()]
        posts.sort(key=lambda p: p.created_at, reverse=True)
        return posts[:limit]
