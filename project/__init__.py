#################
#### imports ####
#################

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap

################
#### config ####
################

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
Bootstrap(app)

if os.environ.get('HEROKU'):
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from .auth.views import auth_blueprint
from .home.views import home_blueprint
from .menu.views import menu_blueprint

# Registro los blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(home_blueprint)
app.register_blueprint(menu_blueprint)


login_manager.login_view = 'auth.login'
