import os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename

from app.models import Post
from app.forms import PostForm
from app.extensions import db

post = Blueprint('posts', __name__, url_prefix='/posts')


@post.get('/<id>')
def show(id):
    post = Post.query.get(id)
    return render_template('posts/show.html', post=post)

@post.get('/new')
def new():
    form = PostForm()
    return render_template('posts/new.html', form=form)

@post.post('/')
def create():
    form = PostForm()

    if form.validate_on_submit():
        image = form.image.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        
        post = Post(title=form.title.data, text=form.text.data,
        published=form.published.data, category_id=form.categories.data, image=filename)
        db.session.add(post)
        db.session.commit()

        flash('Post publicado com sucesso')

        return redirect(url_for('home.index'))
        

    return render_template('posts/new.html', form=form)