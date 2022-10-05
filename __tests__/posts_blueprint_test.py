from ward import test
from flask import url_for

from app.models import Post, Category
from __tests__.fixtures import browser
from __tests__.factories.category_factory import CategoryFactory


@test('Usuário cadastra post', tags=['posts'])
def _(browser=browser):
    category = CategoryFactory.create()

    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Cadastrar postagem').click()
    browser.fill('title', 'Passando as ferias em Salvador-BA')
    browser.fill('text', 'Apenas uma forma de escrever um artigo no blog')
    browser.select('categories', str(category.id))
    browser.check('published')
    browser.attach_file('image', '__tests__/resources/grecia.jpeg')
    browser.find_by_value('Salvar').click()

    assert browser.url == url_for('home.index')
    assert browser.is_text_present('Post publicado com sucesso')
    assert Post.query.first().title == 'Passando as ferias em Salvador-BA'
    assert Post.query.count() == 1
    assert Category.query.first() == Post.query.first().category
