from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random


db = SQLAlchemy()


class User(db.Model):
    # Setup database for Users
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)  # Text() to be hashable
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now())
    # bookmarks = db.relationship("Bookmark", backref="user")

    def __repr__(self):
        # String representation since class should return None
        return f"User>>>{self.username}"


class Jobs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    skill = db.Column(db.String(), nullable=False)
    url = db.Column(db.Text(), nullable=False)
    short_url = db.Column(db.String(3), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now())

    def generate_short_characters(self):
        # string.digits generates numbers 0-9
        # string.ascii_letters generates lower and uppercase letters
        characters = string.digits + string.ascii_letters
        picked_chars = "".join(random.choices(characters, k=3))

        link = self.query.filter_by(short_url=picked_chars).first()

        if link:
            # if the generated characters exists in the db,
            # it will rerun the function until it generated a unique characters
            self.generate_short_characters()
        else:
            return picked_chars

    def __init__(self, **kwargs):
        """
        The super() function is used to give access to methods and properties of a parent or sibling class.

        The super() function returns an object that represents the parent class.
        """
        super().__init__(**kwargs)

        self.short_url = self.generate_short_characters()

    def __repr__(self):
        # String representation since class will return None when called
        return f"Jobs>>>{self.url}"


"""
To execute/create db:
1. Run 'flask shell' on the terminal.
2. On the terminal input:
    $> from src.database import db
    $> db.create_all()
3. To verify:
    $> db
"""
