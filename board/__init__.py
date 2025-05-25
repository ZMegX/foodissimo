# https://realpython.com/videos/scalable-flask-web-app-overview/
import os
from dotenv import load_dotenv
from flask import Flask

from board import pages, posts, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URL"] = os.environ.get("DATABASE_URL")

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")

    return app

