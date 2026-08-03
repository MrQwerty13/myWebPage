from flask import Blueprint, redirect, request, url_for

from i18n import (
    ACCENT_COOKIE,
    COOKIE_MAX_AGE,
    LANG_COOKIE,
    THEME_COOKIE,
    normalize_accent,
    normalize_lang,
    normalize_theme,
)

prefs_bp = Blueprint("prefs", __name__)


def _safe_next() -> str:
    nxt = request.form.get("next") or request.args.get("next") or "/"
    if not nxt.startswith("/") or nxt.startswith("//"):
        return url_for("posts.feed")
    return nxt


@prefs_bp.route("/prefs/theme", methods=["POST"])
def set_theme():
    theme = normalize_theme(request.form.get("theme"))
    response = redirect(_safe_next())
    response.set_cookie(THEME_COOKIE, theme, max_age=COOKIE_MAX_AGE, samesite="Lax")
    return response


@prefs_bp.route("/prefs/lang", methods=["POST"])
def set_lang():
    lang = normalize_lang(request.form.get("lang"))
    response = redirect(_safe_next())
    response.set_cookie(LANG_COOKIE, lang, max_age=COOKIE_MAX_AGE, samesite="Lax")
    return response


@prefs_bp.route("/prefs/accent", methods=["POST"])
def set_accent():
    accent = normalize_accent(request.form.get("accent"))
    response = redirect(_safe_next())
    response.set_cookie(ACCENT_COOKIE, accent, max_age=COOKIE_MAX_AGE, samesite="Lax")
    return response
