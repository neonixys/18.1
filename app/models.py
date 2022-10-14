from flask_restx import fields
from marshmallow import Schema

from app.setup_db import db


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)


class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()


class AuthorSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()




