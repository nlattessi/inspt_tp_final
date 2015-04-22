from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from .forms import LoginForm, RegisterForm
from .. import db
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Username o password invalido", "danger")
            return redirect(url_for('.login'))
        login_user(user, form.remember_me.data)
        flash("Te logueaste con exito.", "success")
        return redirect(request.args.get('next') or url_for('home.user', username=user.username))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Te deslogueaste.", "success")
    return redirect(url_for('home.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            is_admin=form.is_admin.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Te registraste.", "success")
        return redirect(url_for('home.index'))
    return render_template('auth/register.html', form=form)