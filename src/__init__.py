from flask import Flask, jsonify, redirect
import os
from src.database import db
from src.auth import auth
from flask_jwt_extended import JWTManager
from src.constants.http_status_codes import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


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

    # Register the blueprints as an endpoint for the API
    app.register_blueprint(auth)

    @app.errorhandler(HTTP_404_NOT_FOUND)  # You can add errorhandler for any specific errors.
    def handle_404(e):
        """
        Returns a json when a 404 status was encountered.

        Argument:
            e (Required): Exception message

        Return
            json: Error message for the 404 status."""
        return jsonify({"error": "Not found."}), HTTP_404_NOT_FOUND

    return app
    # JWTManager(app)  # For tokens
