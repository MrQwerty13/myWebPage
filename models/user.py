from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from uuid import uuid4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:12]}"


@dataclass
class User:
    id: str
    username: str
    email: str
    password_hash: str
    created_at: str

    @classmethod
    def create(cls, username: str, email: str, password_hash: str) -> User:
        return cls(
            id=new_id("u"),
            username=username.strip(),
            email=email.strip().lower(),
            password_hash=password_hash,
            created_at=utc_now_iso(),
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> User:
        return cls(
            id=data["id"],
            username=data["username"],
            email=data["email"],
            password_hash=data["password_hash"],
            created_at=data["created_at"],
        )

    @classmethod
    def from_row(cls, row) -> User:
        return cls.from_dict(dict(row))

    def public_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at,
        }
