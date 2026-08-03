from __future__ import annotations

from dataclasses import dataclass, asdict

from models.user import new_id, utc_now_iso


@dataclass
class Like:
    id: str
    post_id: str
    user_id: str
    created_at: str

    @classmethod
    def create(cls, post_id: str, user_id: str) -> Like:
        return cls(
            id=new_id("l"),
            post_id=post_id,
            user_id=user_id,
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Like:
        return cls(
            id=data["id"],
            post_id=data["post_id"],
            user_id=data["user_id"],
            created_at=data["created_at"],
        )
