# https://realpython.com/videos/scalable-flask-web-app-overview/
import os
from flask import Flask
from .config import Config
from .database import init_db

from board import pages, posts, database


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from config.py and particularly the DBMS URI

    init_db()

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")

    return app

