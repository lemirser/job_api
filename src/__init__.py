from flask import Flask, jsonify, redirect
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # Setup from .flaskenv
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            SWAGGER={"title": "Bookmarks API", "uiversion": 3},
        )
    else:
        app.config.from_mapping(test_config)

    # DB setup
    db.app = app
    db.init_app(app)

    JWTManager(app)  # For tokens
