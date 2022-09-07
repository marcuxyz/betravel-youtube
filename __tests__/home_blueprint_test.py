from ward import test
from faker import Faker
from flask import url_for

from app import db
from app.models import Post
from __tests__.fixtures import browser


@test('página principal deve está online')
def _(browser=browser):
    browser.visit(url_for('home.index'))    

    assert browser.is_text_present('Olá, Marcus Pereira')


@test('Visitante acessa a página principal e vê posts')
def _(browser=browser):
    faker = Faker()
    post = Post(title=faker.paragraph(), published=True,
                text='text...')
    db.session.add(post)
    db.session.commit()

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)


@test('Visitante não consegue visualizar posts')
def _(browser=browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Nenhum post cadastrado')

