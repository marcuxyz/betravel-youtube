from flask import Blueprint, render_template

from app.models import Post

post = Blueprint('posts', __name__, url_prefix='/posts')


@post.get('/<id>')
def show(id):
    post = Post.query.get(id)
    return render_template('posts/show.html', post=post)