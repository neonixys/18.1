from flask import request
from flask_restx import Namespace, Resource

from app.models import AuthorSchema, Author
from app.setup_db import db

author_ns = Namespace('books')
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

@author_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        all_authors = db.session.query(Author).all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.json
        new_author = Author(**req_json)

        with db.session.begin():
            db.session.add(new_author)

        return "", 201


@author_ns.route('/<int:bid>')
class AuthorsView(Resource):
    def get(self, bid: int):  # Получение данных
        author = db.session.query(Author).filter(Author.id == bid).one()
        return author_schema.dump(author), 200

    def put(self, bid):  # замена данных
        author = db.session.query(Author).get(bid)
        req_json = request.json

        author.first_name = req_json.get("first_name")
        author.last_name = req_json.get("last_name")

        db.session.add(author)
        db.session.commit()

        return "", 204

    def patch(self, bid):  # частичное обновление
        author = db.session.query(Author).get(bid)
        req_json = request.json

        if "first_name" in req_json:
            author.first_name = req_json.get("first_name")
        if "last_name" in req_json:
            author.last_name = req_json.get("last_name")

        db.session.add(author)
        db.session.commit()

        return "", 204

    def delete(self, bid):  # замена данных
        author = db.session.query(Author).get(bid)

        db.session.delete(author)
        db.session.commit()
        return "", 204
