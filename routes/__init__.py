from routes.auth_routes import auth_bp
from routes.post_routes import posts_bp
from routes.like_routes import likes_bp
from routes.prefs_routes import prefs_bp
from routes.mod_routes import mod_bp

__all__ = ["auth_bp", "posts_bp", "likes_bp", "prefs_bp", "mod_bp"]
