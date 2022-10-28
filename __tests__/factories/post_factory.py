import factory
from faker import Faker

from app.extensions import db
from app.models import Post
from .category_factory import CategoryFactory

faker = Faker()


class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    title = factory.Sequence(lambda x: Faker().sentence(nb_words=5))
    text = faker.paragraph(nb_sentences=10)
    published = True
    category = factory.SubFactory(CategoryFactory)
