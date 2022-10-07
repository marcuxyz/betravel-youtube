from flask import render_template, redirect, url_for

from app.forms import CategoryForm
from app.extensions import db
from app.models import Category


class CategoriesController:
    def new(self):
        form = CategoryForm()
        return render_template("categories/new.html", form=form)

    def create(self):
        form = CategoryForm()

        if form.validate_on_submit():
            category = Category(name=form.name.data)
            db.session.add(category)
            db.session.commit()

            return redirect(url_for("home.index"))

        return render_template("categories/new.html", form=form)
