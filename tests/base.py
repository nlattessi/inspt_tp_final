from flask.ext.testing import TestCase

from project import app, db
from project.models import User, MenuCategoria, MenuItem


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.add(MenuCategoria("categoria de test"))
        db.session.add(MenuItem("item de test", 1, 1))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()