from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random


db = SQLAlchemy()


class Skills(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)  # Skill name
    job_title = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return self.name



"""
To execute/create db:
1. Run 'flask shell' on the terminal.
2. On the terminal input:
    $> from src.database import db
    $> db.create_all()
3. To verify:
    $> db
"""
