# blueprint is a Flask class that provides a pattern for grouping related routes (endpoints)
from flask import Blueprint, jsonify, abort, make_response

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1,"book1", "description1"),
    Book(2,"book2", "description2"),
    Book(3,"book3", "description3")
]

all_books_bp = Blueprint("all_books", __name__, url_prefix="/show-all-books")

def valid_input(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"oops, {book_id} is in valid "}, 400))
    for book in books:
        if book_id == book.id:
            return book
    abort(make_response({"message": f"{book_id} is not found"}, 404))
    

@all_books_bp.route("/<book_id>", methods=["GET"])
def get_one_book(book_id):
    book = valid_input(book_id)
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
            }

# creating an endpoint
@all_books_bp.route("", methods=["GET"])
def demonstrate_all_books():
    result_all_books = []
    for book in books:
        result_all_books.append(
            {"id": book.id,
            "title": book.title,
            "description": book.description
            }
        )
    return jsonify(result_all_books), 200