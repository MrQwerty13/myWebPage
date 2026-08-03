from __future__ import annotations

from functools import wraps

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from i18n import translate
from routes.post_routes import _enrich_posts
from services import like_service, post_service

mod_bp = Blueprint("mod", __name__)


def moderation_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("is_moderator"):
            return redirect(url_for("mod.del_home"))
        return view(*args, **kwargs)

    return wrapped


@mod_bp.route("/del", methods=["GET", "POST"])
def del_home():
    if request.method == "POST":
        key = (request.form.get("key") or "").strip()
        expected = current_app.config["MODERATION_KEY"]
        if key == expected:
            session["is_moderator"] = True
            flash(translate("mod.unlocked"), "success")
            return redirect(url_for("mod.del_home"))
        flash(translate("mod.bad_key"), "error")

    if not session.get("is_moderator"):
        return render_template("mod_unlock.html")

    posts = post_service.list_recent(limit=200)
    cards = _enrich_posts(posts, None)
    return render_template("mod_del.html", posts=cards)


@mod_bp.route("/del/<post_id>", methods=["POST"])
@moderation_required
def delete_post(post_id: str):
    deleted = post_service.delete_post(post_id)
    if deleted:
        like_service.delete_for_post(post_id)
        flash(translate("mod.deleted"), "success")
    else:
        flash(translate("flash.post_missing"), "error")
    return redirect(url_for("mod.del_home"))


@mod_bp.route("/del/lock", methods=["POST"])
@moderation_required
def lock():
    session.pop("is_moderator", None)
    flash(translate("mod.locked"), "success")
    return redirect(url_for("mod.del_home"))
