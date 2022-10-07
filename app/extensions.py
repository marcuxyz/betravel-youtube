from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)

    @app.shell_context_processor
    def load_context_processor():
        from app.models import Post

        return dict(
            app=app,
            db=db,
            Post=Post,
        )
