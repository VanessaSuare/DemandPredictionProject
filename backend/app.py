"""Main application entry point for the demand prediction API."""
from flask import Flask
from flask_cors import CORS
from app.routes import app_routes


def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow all origins
    app.register_blueprint(app_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
