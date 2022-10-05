from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField

class PostForm(FlaskForm):
    title = StringField('Nome')
    text = StringField('Nome')
    published = BooleanField('Publicar')
    submit = SubmitField('Salvar')

class CategoryForm(FlaskForm):
    name = StringField('Nome')
    submit = SubmitField('Salvar')