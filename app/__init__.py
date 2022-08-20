from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dynaconf import FlaskDynaconf


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list=True)
    
    from app import routes

    routes.init_app(app)
    db.init_app(app)
    
    return app