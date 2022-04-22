# blueprint is a Flask class that provides a pattern for grouping related routes (endpoints)
from flask import Blueprint,jsonify

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

all_books_bp = Blueprint("all_books", __name__)


# creating an endpoint
@all_books_bp.route("/show-all-books", methods=["GET"])
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