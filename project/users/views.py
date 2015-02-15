#################
#### imports ####
#################

from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint # pragma: no cover
from functools import wraps # pragma: no cover
# ACA VA BRCYPT
# from flask.ext.bcrypt import Bcrypt
from passlib.hash import sha256_crypt # pragma: no cover
from flask.ext.login import login_user, login_required, logout_user # pragma: no cover
from .forms import LoginForm, RegisterForm # pragma: no cover
from .. import db # pragma: no cover
from ..models import User # pragma: no cover
#from app import app
#from flask.ext.sqlalchemy import SQLAlchemy




#### config ####

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
) # pragma: no cover


#### rutas ####

@users_blueprint.route('/login', methods=['GET', 'POST']) # pragma: no cover
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is not None and sha256_crypt.verify(request.form['password'], user.password):
                login_user(user)
                flash('Acabas de loguearte!')
                return redirect(url_for('home.home'))
            else:
                error = 'Credenciales invalidas. Proba de nuevo'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout') # pragma: no cover
@login_required # pragma: no cover
def logout():
    #session.pop('logged_in', None)
    logout_user()
    flash('Acabas de desloguearte!')
    return redirect(url_for('home.welcome'))


@users_blueprint.route('/register', methods=['GET', 'POST']) # pragma: no cover
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)