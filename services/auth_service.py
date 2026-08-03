from __future__ import annotations

from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from storage import likes_store, posts_store, users_store


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

    def authenticate(self, email: str, password: str) -> User:
        email = email.strip().lower()
        raw = users_store.find(lambda u: u["email"] == email)
        if not raw:
            raise AuthError("invalid_credentials")

        user = User.from_dict(raw)
        if not check_password_hash(user.password_hash, password):
            raise AuthError("invalid_credentials")
        return user

    def verify_password(self, user: User, password: str) -> bool:
        return check_password_hash(user.password_hash, password)

    def delete_account(self, user_id: str) -> bool:
        raw = users_store.find(lambda u: u["id"] == user_id)
        if not raw:
            return False

        post_ids = {
            post["id"]
            for post in posts_store.filter(lambda p: p["author_id"] == user_id)
        }
        likes_store.delete_where(
            lambda like: like["user_id"] == user_id or like["post_id"] in post_ids
        )
        posts_store.delete_where(lambda post: post["author_id"] == user_id)
        users_store.delete_where(lambda u: u["id"] == user_id)
        return True

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
