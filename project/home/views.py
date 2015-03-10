#################
#### imports ####
#################

from flask import render_template, Blueprint


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


@home_blueprint.route('/')
def index():
    return render_template('index.html')


@home_blueprint.route('/prueba')
def prueba():
    return render_template('prueba.html')