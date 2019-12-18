from flask_testing import TestCase
from app import create_app

app, manager, db = create_app()

session = db.session


class BaseTest(TestCase):
    """
    测试基类
    """
    def create_app(self):
        flask_app = app.app
        flask_app.config['TESTING'] = True
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
        return flask_app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
