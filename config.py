# Default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xdeF\x8c\xe8wuU\xdc\x1b\xae\x0e\xf8\xfa\xe2\xd2\x8c|\xf3\x9a\xceL\x1c\xd2\n'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    PORT = 8000


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False