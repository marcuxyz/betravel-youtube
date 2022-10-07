from ward import test
from flask import url_for

from app.models import Category
from __tests__.fixtures import browser


@test("Usuário cadastra categoria", tags=["categories"])
def _(browser=browser):
    browser.visit(url_for("home.index"))
    browser.links.find_by_text("Cadastrar categoria").click()
    browser.fill("name", "Europa")
    browser.find_by_value("Salvar").click()

    assert browser.url == url_for("home.index")
    assert Category.query.first().name == "Europa"
    assert Category.query.count() == 1
