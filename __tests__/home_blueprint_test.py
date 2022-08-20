from ward import test

from app import db
from app.models import Post
from __tests__.fixtures import browser


@test('página principal deve está online')
def _(browser=browser):
    browser.visit('/')    

    assert browser.is_text_present('Olá, Marcus Pereira')


@test('Visitante acessa a página principal e vê posts')
def _(browser=browser):
    post = Post(title='Curtindo as ferias em Salvador', published=True,
                text='text...')
    db.session.add(post)
    db.session.commit()
        
    browser.visit('/')

    assert browser.is_text_present('Curtindo as ferias em Salvador')

