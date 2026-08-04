from __future__ import annotations

from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from storage import connect


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

        with connect() as conn:
            if conn.execute(
                "SELECT 1 FROM users WHERE lower(username) = lower(?)",
                (username,),
            ).fetchone():
                raise AuthError("username_taken")
            if conn.execute(
                "SELECT 1 FROM users WHERE email = ?",
                (email,),
            ).fetchone():
                raise AuthError("email_taken")

            user = User.create(
                username=username,
                email=email,
                password_hash=generate_password_hash(password, method="pbkdf2:sha256"),
            )
            conn.execute(
                """
                INSERT INTO users (id, username, email, password_hash, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    user.id,
                    user.username,
                    user.email,
                    user.password_hash,
                    user.created_at,
                ),
            )
            return user

    def authenticate(self, email: str, password: str) -> User:
        email = email.strip().lower()
        with connect() as conn:
            row = conn.execute(
                "SELECT * FROM users WHERE email = ?",
                (email,),
            ).fetchone()

        if not row:
            raise AuthError("invalid_credentials")

        user = User.from_row(row)
        if not check_password_hash(user.password_hash, password):
            raise AuthError("invalid_credentials")
        return user

    def verify_password(self, user: User, password: str) -> bool:
        return check_password_hash(user.password_hash, password)

    def delete_account(self, user_id: str) -> bool:
        with connect() as conn:
            row = conn.execute(
                "SELECT id FROM users WHERE id = ?",
                (user_id,),
            ).fetchone()
            if not row:
                return False
            # Cascades remove this user's posts, likes, and comments;
            # posts they authored also cascade their likes/comments.
            conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            return True

    def get_by_id(self, user_id: str) -> User | None:
        with connect() as conn:
            row = conn.execute(
                "SELECT * FROM users WHERE id = ?",
                (user_id,),
            ).fetchone()
        return User.from_row(row) if row else None

    def get_by_ids(self, user_ids: set[str]) -> dict[str, User]:
        if not user_ids:
            return {}
        placeholders = ",".join("?" for _ in user_ids)
        with connect() as conn:
            rows = conn.execute(
                f"SELECT * FROM users WHERE id IN ({placeholders})",
                tuple(user_ids),
            ).fetchall()
        return {row["id"]: User.from_row(row) for row in rows}
