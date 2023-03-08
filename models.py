from __init__ import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column("First Name", db.String(128), nullable=False)
    email = db.Column("Email", db.String(128),
                      unique=True, nullable=False)
    password = db.Column("Password", db.String(128),
                         unique=True, nullable=False)

    def __init__(self, first_name, email, password):
        self.first_name = first_name
        self.email = email
        self.password = password
