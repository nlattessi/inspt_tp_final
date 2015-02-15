import os

# Default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xdeF\x8c\xe8wuU\xdc\x1b\xae\x0e\xf8\xfa\xe2\xd2\x8c|\xf3\x9a\xceL\x1c\xd2\n'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'


class ProductionConfig(BaseConfig):
    DEBUG = False
    if os.environ.get('HEROKU'):
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']