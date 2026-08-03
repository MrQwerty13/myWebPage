from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from routes.helpers import login_required
from services import AuthError, auth_service

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if g.user:
        return redirect(url_for("posts.feed"))

    if request.method == "POST":
        username = request.form.get("username", "")
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        try:
            user = auth_service.create_user(username, email, password)
            session.clear()
            session["user_id"] = user.id
            flash("Welcome to Aftertaste.", "success")
            return redirect(url_for("posts.feed"))
        except AuthError as exc:
            flash(str(exc), "error")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if g.user:
        return redirect(url_for("posts.feed"))

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        try:
            user = auth_service.authenticate(username, password)
            session.clear()
            session["user_id"] = user.id
            flash(f"Hey, {user.username}.", "success")
            return redirect(url_for("posts.feed"))
        except AuthError as exc:
            flash(str(exc), "error")

    return render_template("login.html")


@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    flash("Signed out.", "success")
    return redirect(url_for("posts.feed"))
