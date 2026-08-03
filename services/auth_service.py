from __future__ import annotations

from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from storage import users_store


class AuthError(Exception):
    pass


class AuthService:
    def create_user(self, username: str, email: str, password: str) -> User:
        username = username.strip()
        email = email.strip().lower()

        if len(username) < 3:
            raise AuthError("username_too_short")
        if "@" not in email or "." not in email:
            raise AuthError("email_invalid")
        if len(password) < 6:
            raise AuthError("password_too_short")

        if users_store.find(lambda u: u["username"].lower() == username.lower()):
            raise AuthError("username_taken")
        if users_store.find(lambda u: u["email"] == email):
            raise AuthError("email_taken")

        user = User.create(
            username=username,
            email=email,
            password_hash=generate_password_hash(password, method="pbkdf2:sha256"),
        )
        users_store.append(user.to_dict())
        return user

    def authenticate(self, username: str, password: str) -> User:
        username = username.strip()
        raw = users_store.find(lambda u: u["username"].lower() == username.lower())
        if not raw:
            raise AuthError("invalid_credentials")

        user = User.from_dict(raw)
        if not check_password_hash(user.password_hash, password):
            raise AuthError("invalid_credentials")
        return user

    def get_by_id(self, user_id: str) -> User | None:
        raw = users_store.find(lambda u: u["id"] == user_id)
        return User.from_dict(raw) if raw else None

    def get_by_ids(self, user_ids: set[str]) -> dict[str, User]:
        if not user_ids:
            return {}
        users: dict[str, User] = {}
        for raw in users_store.all():
            user_id = raw["id"]
            if user_id in user_ids:
                users[user_id] = User.from_dict(raw)
                if len(users) == len(user_ids):
                    break
        return users
