from __future__ import annotations

from dataclasses import dataclass, asdict

from models.user import new_id, utc_now_iso


@dataclass
class Post:
    id: str
    author_id: str
    drink_name: str
    content: str
    created_at: str

    @classmethod
    def create(cls, author_id: str, drink_name: str, content: str) -> Post:
        return cls(
            id=new_id("p"),
            author_id=author_id,
            drink_name=drink_name.strip(),
            content=content.strip(),
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Post:
        return cls(
            id=data["id"],
            author_id=data["author_id"],
            drink_name=data["drink_name"],
            content=data["content"],
            created_at=data["created_at"],
        )
