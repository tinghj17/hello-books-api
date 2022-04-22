from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    # register the Blueprint: tell the app that it should use the endpoints from all_books_bp for its routing
    from .route import all_books_bp
    app.register_blueprint(all_books_bp)
    
    return app