from flask import render_template

from app.models import Post

class HomeController:
    def index(self):
        posts = Post.query.filter_by(published=True).all()
        return render_template('home/index.html', posts=posts)