import os

from flask import Flask

from i18n import current_accent, current_lang, current_theme, translate
from i18n.translations import ACCENT_SWATCHES, SUPPORTED_ACCENTS
from routes import auth_bp, likes_bp, mod_bp, posts_bp, prefs_bp
from routes.helpers import load_request_context


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY",
        "aftertaste-dev-secret-change-me",
    )
    app.config["MODERATION_KEY"] = os.environ.get(
        "MODERATION_KEY",
        "wanna_clean",
    )

    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(likes_bp)
    app.register_blueprint(prefs_bp)
    app.register_blueprint(mod_bp)

    app.before_request(load_request_context)

    @app.context_processor
    def inject_i18n():
        return {
            "_": translate,
            "theme": current_theme(),
            "lang": current_lang(),
            "accent": current_accent(),
            "accents": SUPPORTED_ACCENTS,
            "accent_swatches": ACCENT_SWATCHES,
        }

    return app


app = create_app()

if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(port=int(os.environ.get("PORT", "8080")), debug=debug)
