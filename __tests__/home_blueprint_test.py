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

@test('Visitante ver post')
def _(browser=browser):
    post = PostFactory.create()

    browser.visit(url_for('home.index'))
    browser.links.find_by_text(post.title).click()

    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.text)


@test('Visitante acessa a página principal e não ver posts não publicados')
def _(browser=browser):
    post = PostFactory.create(title='Curtindo as ferias em Salvador')
    drafts = PostFactory.create_batch(2, published=False)

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)
    assert browser.is_text_not_present(drafts[0].title)
    assert browser.is_text_not_present(drafts[1].title)


@test('Visitante não consegue visualizar posts')
def _(browser=browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Nenhum post cadastrado')

