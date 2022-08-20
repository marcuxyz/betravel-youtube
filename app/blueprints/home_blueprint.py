from flask import Blueprint

from app.models import Post

home = Blueprint("home", __name__)


@home.route('/')
def index():
    post = Post.query.first() # select * from post limit 1;
    return post.title