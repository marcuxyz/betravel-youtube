from ward import test
from flask import url_for

from app.models import Post
from __tests__.fixtures import browser



@test('Usuário cadastra post', tags=['posts'])
def _(browser=browser):
    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Cadastrar postagem').click()
    browser.fill('title', 'Passando as ferias em Salvador-BA')
    browser.fill('text', 'Apenas uma forma de escrever um artigo no blog')
    browser.check('published')
    browser.find_by_value('Salvar').click()

    assert browser.url == url_for('home.index')
    assert browser.is_text_present('Post publicado com sucesso')
    assert Post.query.first().title == 'Passando as ferias em Salvador-BA'
    assert Post.query.count() == 1
