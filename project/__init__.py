#################
#### imports ####
#################

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

################
#### config ####
################

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

if os.environ.get('HEROKU'):
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# Registro los blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from .models import User

login_manager.login_view = 'users.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()