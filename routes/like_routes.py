from flask import Blueprint, g, jsonify

from routes.helpers import login_required
from services import like_service, post_service

likes_bp = Blueprint("likes", __name__)


@likes_bp.route("/posts/<post_id>/like", methods=["POST"])
@login_required
def toggle_like(post_id: str):
    post = post_service.get_by_id(post_id)
    if not post:
        return jsonify({"error": "Post not found."}), 404

    result = like_service.toggle_like(post_id=post_id, user_id=g.user.id)
    return jsonify(result)
