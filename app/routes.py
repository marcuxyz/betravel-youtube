from app.blueprints.home_blueprint import home


def init_app(app):
    app.register_blueprint(home)