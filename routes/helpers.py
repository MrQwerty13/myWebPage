from functools import wraps

from flask import flash, g, jsonify, redirect, request, session, url_for

from services import auth_service


def load_current_user():
    user_id = session.get("user_id")
    g.user = auth_service.get_by_id(user_id) if user_id else None


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            wants_json = "application/json" in (request.headers.get("Accept") or "")
            if wants_json or request.path.endswith("/like"):
                return jsonify({"error": "Authentication required."}), 401
            flash("Log in to continue.", "error")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped
