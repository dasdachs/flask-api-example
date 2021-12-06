from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

import config


db = SQLAlchemy()


def create_app(env: str = "development") -> Flask:
    app = Flask(__name__)

    if env == "production":
        app.config.from_object(config.ProductionConfig)
    elif env == "testing":
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)

    with app.app_context():
        from models import Post

        db.create_all()

        @app.route("/api/v1/posts", methods=["GET", "POST"])
        def list_or_create_posts():
            if request.method == "POST":
                body = request.get_json()
                post = Post(
                    title=body.get("title"),
                    body=body.get("body")
                )

                db.session.add(post)
                db.session.commit()

                return jsonify(post), 201

            posts = Post.query.all()

            return jsonify([post.to_json() for post in posts])

        @app.route("/")
        def index():
            return render_template("index.html")

        return app

