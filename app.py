from flask import Flask

from routes import auth_bp, likes_bp, posts_bp
from routes.helpers import load_current_user


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "aftertaste-dev-secret-change-me"

    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(likes_bp)

    app.before_request(load_current_user)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
