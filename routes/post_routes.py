from __future__ import annotations

from datetime import datetime

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
)

from i18n import current_lang, translate
from routes.helpers import login_required
from services import (
    CommentError,
    PostError,
    auth_service,
    comment_service,
    like_service,
    post_service,
)

posts_bp = Blueprint("posts", __name__)


def _format_when(iso_value: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_value)
        if current_lang() == "ru":
            return dt.strftime("%d.%m.%Y · %H:%M")
        return dt.strftime("%b %d, %Y · %H:%M")
    except ValueError:
        return iso_value


def _enrich_posts(posts, current_user_id: str | None):
    if not posts:
        return []

    post_ids = {post.id for post in posts}
    authors = auth_service.get_by_ids({post.author_id for post in posts})
    like_counts, liked_ids = like_service.stats_for_feed(post_ids, current_user_id)
    comment_counts = comment_service.counts_for_posts(post_ids)

    cards = []
    for post in posts:
        author = authors.get(post.author_id)
        cards.append(
            {
                "id": post.id,
                "author_id": post.author_id,
                "drink_name": post.drink_name,
                "content": post.content,
                "created_label": _format_when(post.created_at),
                "updated_label": (
                    _format_when(post.updated_at) if post.updated_at else None
                ),
                "edited": bool(post.updated_at),
                "author_name": author.username if author else translate("unknown_author"),
                "like_count": like_counts.get(post.id, 0),
                "comment_count": comment_counts.get(post.id, 0),
                "liked": post.id in liked_ids,
                "is_owner": bool(
                    current_user_id and current_user_id == post.author_id
                ),
            }
        )
    return cards


def _enrich_comments(comments, current_user_id: str | None):
    if not comments:
        return []
    authors = auth_service.get_by_ids({c.author_id for c in comments})
    cards = []
    for comment in comments:
        author = authors.get(comment.author_id)
        cards.append(
            {
                "id": comment.id,
                "content": comment.content,
                "created_label": _format_when(comment.created_at),
                "author_name": author.username if author else translate("unknown_author"),
                "is_owner": bool(
                    current_user_id and current_user_id == comment.author_id
                ),
            }
        )
    return cards


@posts_bp.route("/")
def feed():
    posts = post_service.list_recent()
    cards = _enrich_posts(posts, g.user.id if g.user else None)
    return render_template("feed.html", posts=cards)


@posts_bp.route("/about")
def about():
    return render_template("about.html")


@posts_bp.route("/posts/new", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        drink_name = request.form.get("drink_name", "")
        content = request.form.get("content", "")
        try:
            post = post_service.create_post(g.user.id, drink_name, content)
            flash(translate("flash.post_live"), "success")
            return redirect(url_for("posts.detail", post_id=post.id))
        except PostError as exc:
            flash(translate(str(exc)), "error")
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
        flash(translate("flash.post_missing"), "error")
        return redirect(url_for("posts.feed"))

    user_id = g.user.id if g.user else None
    cards = _enrich_posts([post], user_id)
    comments = _enrich_comments(comment_service.list_for_post(post_id), user_id)
    return render_template("post_detail.html", post=cards[0], comments=comments)


@posts_bp.route("/posts/<post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id: str):
    post = post_service.get_by_id(post_id)
    if not post:
        flash(translate("flash.post_missing"), "error")
        return redirect(url_for("posts.feed"))
    if post.author_id != g.user.id:
        flash(translate("post_forbidden"), "error")
        return redirect(url_for("posts.detail", post_id=post_id))

    if request.method == "POST":
        drink_name = request.form.get("drink_name", "")
        content = request.form.get("content", "")
        try:
            post_service.update_post(post_id, g.user.id, drink_name, content)
            flash(translate("flash.post_updated"), "success")
            return redirect(url_for("posts.detail", post_id=post_id))
        except PostError as exc:
            flash(translate(str(exc)), "error")
            return render_template(
                "edit_post.html",
                post_id=post_id,
                drink_name=drink_name,
                content=content,
            )

    return render_template(
        "edit_post.html",
        post_id=post.id,
        drink_name=post.drink_name,
        content=post.content,
    )


@posts_bp.route("/posts/<post_id>/delete", methods=["POST"])
@login_required
def delete_own_post(post_id: str):
    try:
        deleted = post_service.delete_post(post_id, author_id=g.user.id)
    except PostError as exc:
        flash(translate(str(exc)), "error")
        return redirect(url_for("posts.detail", post_id=post_id))

    if deleted:
        flash(translate("flash.post_deleted"), "success")
    else:
        flash(translate("flash.post_missing"), "error")
    return redirect(url_for("posts.feed"))


@posts_bp.route("/posts/<post_id>/comments", methods=["POST"])
@login_required
def add_comment(post_id: str):
    content = request.form.get("content", "")
    try:
        comment_service.create_comment(post_id, g.user.id, content)
        flash(translate("flash.comment_added"), "success")
    except CommentError as exc:
        flash(translate(str(exc)), "error")
    return redirect(url_for("posts.detail", post_id=post_id))


@posts_bp.route("/posts/<post_id>/comments/<comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(post_id: str, comment_id: str):
    try:
        deleted = comment_service.delete_comment(comment_id, author_id=g.user.id)
    except CommentError as exc:
        flash(translate(str(exc)), "error")
        return redirect(url_for("posts.detail", post_id=post_id))

    if deleted:
        flash(translate("flash.comment_deleted"), "success")
    else:
        flash(translate("flash.comment_missing"), "error")
    return redirect(url_for("posts.detail", post_id=post_id))
