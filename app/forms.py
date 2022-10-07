from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    SubmitField,
    BooleanField,
    SelectField,
    FileField,
    TextAreaField,
)

from app.models import Category


class PostForm(FlaskForm):
    title = StringField("Título")
    text = TextAreaField("Conteúdo")
    published = BooleanField("Publicar")
    categories = SelectField("Categorias", coerce=int)
    image = FileField("Imagem")
    submit = SubmitField("Salvar")

    def __init__(self):
        super(PostForm, self).__init__()
        self.categories.choices = [
            (c.id, c.name) for c in Category.query.all()
        ]


class CategoryForm(FlaskForm):
    name = StringField("Nome")
    submit = SubmitField("Salvar")
