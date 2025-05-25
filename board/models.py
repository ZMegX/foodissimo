# board/models.py
from board.database import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), default="Anonymous")
    message = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)