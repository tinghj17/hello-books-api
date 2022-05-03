from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/my_hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.book import Book

    # register the Blueprint: tell the app that it should use the endpoints from all_books_bp for its routing
    from .route import all_books_bp
    app.register_blueprint(all_books_bp)
    
    return app