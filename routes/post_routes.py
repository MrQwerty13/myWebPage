from __future__ import annotations

from datetime import datetime

from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from routes.helpers import login_required
from services import PostError, auth_service, like_service, post_service

posts_bp = Blueprint("posts", __name__)


def _format_when(iso_value: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_value)
        return dt.strftime("%b %d, %Y · %H:%M")
    except ValueError:
        return iso_value


def _enrich_posts(posts, current_user_id: str | None):
    authors = auth_service.get_by_ids({post.author_id for post in posts})
    like_counts = like_service.count_by_post()
    liked_ids = (
        like_service.liked_post_ids_for_user(current_user_id)
        if current_user_id
        else set()
    )

    cards = []
    for post in posts:
        author = authors.get(post.author_id)
        cards.append(
            {
                "id": post.id,
                "drink_name": post.drink_name,
                "content": post.content,
                "created_at": post.created_at,
                "created_label": _format_when(post.created_at),
                "author_name": author.username if author else "Unknown",
                "like_count": like_counts.get(post.id, 0),
                "liked": post.id in liked_ids,
            }
        )
    return cards


@posts_bp.route("/")
def feed():
    posts = post_service.list_recent()
    cards = _enrich_posts(posts, g.user.id if g.user else None)
    return render_template("feed.html", posts=cards)


@posts_bp.route("/posts/new", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        drink_name = request.form.get("drink_name", "")
        content = request.form.get("content", "")
        try:
            post = post_service.create_post(g.user.id, drink_name, content)
            flash("Your take is live.", "success")
            return redirect(url_for("posts.detail", post_id=post.id))
        except PostError as exc:
            flash(str(exc), "error")
            return render_template(
                "new_post.html",
                drink_name=drink_name,
                content=content,
            )

    return render_template("new_post.html", drink_name="", content="")


@posts_bp.route("/posts/<post_id>")
def detail(post_id: str):
    post = post_service.get_by_id(post_id)
    if not post:
        flash("Post not found.", "error")
        return redirect(url_for("posts.feed"))

    cards = _enrich_posts([post], g.user.id if g.user else None)
    return render_template("post_detail.html", post=cards[0])
