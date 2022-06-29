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
    pass
