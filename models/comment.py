from __future__ import annotations

from dataclasses import asdict, dataclass

from models.user import new_id, utc_now_iso


@dataclass
class Comment:
    id: str
    post_id: str
    author_id: str
    content: str
    created_at: str

    @classmethod
    def create(cls, post_id: str, author_id: str, content: str) -> Comment:
        return cls(
            id=new_id("c"),
            post_id=post_id,
            author_id=author_id,
            content=content.strip(),
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Comment:
        return cls(
            id=data["id"],
            post_id=data["post_id"],
            author_id=data["author_id"],
            content=data["content"],
            created_at=data["created_at"],
        )

    @classmethod
    def from_row(cls, row) -> Comment:
        return cls.from_dict(dict(row))
