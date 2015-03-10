import os

# Default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'secret key'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    BOOTSTRAP_SERVE_LOCAL = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    if os.environ.get('HEROKU'):
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']