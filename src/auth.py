from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from src.database import db, User
from src.constants.http_status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_409_CONFLICT,
)

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post("/register")
def register():
    """
    Register the user details in the database if they meet the requirements during the registration.

    Requirements:
        Username:
            1. Username should have more than 3 characters.
            2. Doesn't have any whitespace and should only contain alphanumeric.
            3. Username should be unique.

        Password:
            1. Should be more than 6 characters.

        Email:
            1. Should be a valid email format.
            2. Email should be unique or doesn't already exists in the database.

    Returns;
        jsonify: Returns a successful message and displays the user details.
    """
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    if len(username) < 3:
        return jsonify({"error": "Username is too short!"}), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:  # .isalnum() is for alphanumeric
        return (
            jsonify({"error": "Username should be alphanumeric or does not contain any spaces!"}),
            HTTP_400_BAD_REQUEST,
        )

    # Check if the username already exist in the database
    if User.query.filter_by(username=username).first() is not None:
        return (
            jsonify({"error": "Username is already taken!"}),
            HTTP_409_CONFLICT,
        )

    if len(password) < 6:
        return jsonify({"error": "Password is too short!"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({"error": "Email is not valid!"}), HTTP_400_BAD_REQUEST

    # Check if the email already exist in the database
    if User.query.filter_by(email=email).first() is not None:
        return (
            jsonify({"error": "Email is already taken!"}),
            HTTP_409_CONFLICT,
        )

    # Generate a hash for the password
    pwd_hash = generate_password_hash(password)

    user = User(username=username, password=pwd_hash, email=email)

    # Add the user details to the session
    db.session.add(user)
    db.session.commit()

    return (
        jsonify({"message": "User was created successfully!", "user": {"username": username, "email": email}}),
        HTTP_201_CREATED,
    )
