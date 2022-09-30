from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField

class CategoryForm(FlaskForm):
    name = StringField('Nome')
    submit = SubmitField('Salvar')