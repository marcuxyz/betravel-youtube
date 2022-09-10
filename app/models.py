from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    published = db.Column(db.Boolean, default=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return self.title