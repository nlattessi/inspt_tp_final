from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .categorias import categorias as categorias_blueprint
    app.register_blueprint(categorias_blueprint, url_prefix='/categorias')

    from .items import items as items_blueprint
    app.register_blueprint(items_blueprint, url_prefix='/items')

    from .pedidos import pedidos as pedidos_blueprint
    app.register_blueprint(pedidos_blueprint, url_prefix='/pedidos')

    # from .api_1_0 import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api/1.0')

    return app