# https://realpython.com/videos/scalable-flask-web-app-overview/
import os
from flask import Flask
from .config import Config
from board.database import db

from board import pages, posts


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from config.py and particularly the DBMS URI

    db.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
   
    return app

