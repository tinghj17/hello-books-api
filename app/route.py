# blueprint is a Flask class that provides a pattern for grouping related routes (endpoints)
from wsgiref.util import request_uri
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request


# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1,"book1", "description1"),
#     Book(2,"book2", "description2"),
#     Book(3,"book3", "description3")
# ]

all_books_bp = Blueprint("all_books", __name__, url_prefix="/show-all-books")

# helper function
def valid_input(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"oops, {book_id} is in valid "}, 400))
    book = Book.query.get(book_id)
    
    if not book:
        abort(make_response({"message": f"{book_id} is not found"}, 404))
    return book
    
@all_books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])
    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)


# @all_books_bp.route("/<book_id>", methods=["GET"])
# def get_one_book(book_id):
#     book = valid_input(book_id)
#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#             }

# creating an endpoint
@all_books_bp.route("", methods=["GET"])
def demonstrate_all_books():
    books = Book.query.all()
    result_all_books = []
    for book in books:
        result_all_books.append(
            {"id": book.id,
            "title": book.title,
            "description": book.description
            }
        )
    return jsonify(result_all_books), 200

@all_books_bp.route("<book_id>", methods=["GET"])
def get_one_book(book_id):
    book = valid_input(book_id)
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }

@all_books_bp.route("<book_id>", methods=["PUT"])
def update_book(book_id):
    book = valid_input(book_id)

    request_body = request.get_json()
    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book {book.title} successfully updated", 201)

@all_books_bp.route("<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = valid_input(book_id)
    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book {book.title} successfully deleted", 201)




