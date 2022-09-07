from ward import test
from flask import url_for

from __tests__.factories.post_factory import PostFactory
from __tests__.fixtures import browser


@test('página principal deve está online')
def _(browser=browser):
    browser.visit(url_for('home.index'))    

    assert browser.is_text_present('Olá, Marcus Pereira')


@test('Visitante acessa a página principal e vê posts')
def _(browser=browser):
    post = PostFactory.create()

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)


@test('Visitante não consegue visualizar posts')
def _(browser=browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Nenhum post cadastrado')

