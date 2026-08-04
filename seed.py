"""Seed a couple of demo users and posts for local testing."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from services import auth_service, comment_service, like_service, post_service
from storage import connect, init_db


def main() -> None:
    init_db()
    with connect() as conn:
        conn.execute("DELETE FROM comments")
        conn.execute("DELETE FROM likes")
        conn.execute("DELETE FROM posts")
        conn.execute("DELETE FROM users")

    anna = auth_service.create_user("anna", "anna@example.com", "password")
    leo = auth_service.create_user("leo", "leo@example.com", "password")

    p1 = post_service.create_post(
        anna.id,
        "Oat flat white",
        "Silky, a little sweet from the oat milk, espresso still clear underneath. Morning keeper.",
    )
    p2 = post_service.create_post(
        leo.id,
        "Negroni",
        "Bitter orange forward, gin shows late. Best with one big ice cube and nowhere to be.",
    )
    post_service.create_post(
        anna.id,
        "Hojicha latte",
        "Toasty, almost cocoa-like, very soft caffeine. Perfect rainy afternoon drink.",
    )

    like_service.toggle_like(p1.id, leo.id)
    like_service.toggle_like(p2.id, anna.id)

    comment_service.create_comment(
        p1.id,
        leo.id,
        "That oat milk texture is exactly what I chase on weekday mornings.",
    )
    comment_service.create_comment(
        p2.id,
        anna.id,
        "Agree on the big ice cube — keeps the bitterness honest.",
    )

    print("Seeded users: anna@example.com / leo@example.com (password: password)")
    print("Seeded 3 posts, likes, and comments.")


if __name__ == "__main__":
    main()
