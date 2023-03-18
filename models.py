from app import db
from flask_login import UserMixin
from datetime import datetime

categories_notes = db.Table('Categories_notes', db.metadata, db.Column('id', db.Integer, primary_key=True),
                            db.Column('Category_id', db.Integer,
                                      db.ForeignKey('Categories.id')),
                            db.Column('Note_id', db.Integer, db.ForeignKey('Notes.id')))


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


class Category(db.Model):
    __tablename__ = "Categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String(256), nullable=False)
    notes = db.relationship(
        'Note', secondary=categories_notes, back_populates="categories")

    def __init__(self, title):
        self.title = title


class Note(db.Model):
    __tablename__ = "Notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String(256), nullable=False)
    text = db.Column("Text", db.String(2048), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    picture = db.Column("Picture", db.Boolean, default=True)
    user_id = db.Column("User id", db.Integer, db.ForeignKey('Users.id'))
    user = db.relationship("User")
    categories = db.relationship(
        'Category', secondary=categories_notes, back_populates="notes")

    def __init__(self, title, text, user_id, date=None, picture=None):
        self.title = title
        self.text = text
        self.date = date
        self.picture = picture
        self.user_id = user_id
