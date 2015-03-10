#################
#### imports ####
#################

from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint
from flask.ext.login import login_user, login_required, logout_user
from .forms import LoginForm, RegisterForm
from .. import db
from ..models import User


################
#### config ####
################

auth_blueprint = Blueprint(
    'auth', __name__,
    template_folder='templates'
)


###############
#### rutas ####
###############

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Email o password invalido.")
            return redirect(url_for('.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('menu.index'))
    return render_template('login.html', form=form)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Acabas de desloguearte!')
    return redirect(url_for('home.index'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('menu.menu'))
    return render_template('register.html', form=form)


@auth_blueprint.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)