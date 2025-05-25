# create blueprints routes for the form
# user can input data through those routes
from flask import (
    Blueprint, render_template,
    redirect, request, url_for
)

from board.database import db
from board.models import Post

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form.get["author"] or "Anonymous"
        message = request.form.get["message"]
        if message:
            new_post = Post(author=author, message=message)          
            db.session.add(new_post) #with SQLAlchemy we need to us db.session to add/edit
            db.session.commit()
            return redirect(url_for("posts.posts"))
        
    return render_template("posts/create.html")


@bp.route("/posts")
def posts():
    posts = Post.query.order_by(Post.created.desc().all) # query from the post model created
    return render_template("posts/posts.html", posts=posts)