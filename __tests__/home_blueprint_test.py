from ward import test
from splinter import Browser

from app import create_app

@test('página principal deve está online')
def _():
    app = create_app()
    app.testing = True
    browser = Browser("flask", app=app)

    browser.visit('/')    
    assert browser.is_text_present('Olá, Marcus Pereira')