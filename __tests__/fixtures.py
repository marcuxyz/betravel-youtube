from splinter import Browser
from ward import fixture
from dotenv import load_dotenv

from app import create_app
from app.extensions import db

load_dotenv(".env.test")


@fixture
def browser():
    app = create_app()
    app.testing = True
    context = app.test_request_context()
    context.push()

    with app.test_client():
        db.create_all()

        yield Browser("flask", app=app)

        db.drop_all()
        db.session.remove()
