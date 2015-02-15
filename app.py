# #################
# #### imports ####
# #################

# from flask import Flask, render_template, request, redirect, url_for, session, flash, g
# from flask.ext.sqlalchemy import SQLAlchemy
# # ACA VA BRCYPT
# # from flask.ext.bcrypt import Bcrypt
# from passlib.hash import sha256_crypt
# from functools import wraps

# ################
# #### config ####
# ################

# # Creo el objeto Flask
# app = Flask(__name__)
# app.config.from_object('config.DevelopmentConfig')
# db = SQLAlchemy(app)

# from models import *
# from project.users.views import users_blueprint

# # Registro los blueprints
# app.register_blueprint(users_blueprint)


# #### helper functions ####

# # Decorador de login
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Tenes que loeguarte primero.')
#             return redirect(url_for('users.login'))
#     return wrap


# @app.route('/')
# @login_required
# def home():
#     #return render_template('index.html')
#     # g.db = connect_db()
#     # cur = g.db.execute('select * from menu_items')
#     # menu_items = [dict(nombre=row[0], precio=row[1]) for row in cur.fetchall()]
#     # g.db.close()
#     menu_items = db.session.query(MenuItem).all()
#     return render_template('index.html', menu_items=menu_items)


# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')


# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     error = None
# #     if request.method == 'POST':
# #         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
# #             error = 'Credenciales invalidas. Proba de nuevo'
# #         else:
# #             session['logged_in'] = True
# #             flash('Acabas de loguearte!')
# #             return redirect(url_for('home'))
# #     return render_template('login.html', error=error)


# # @app.route('/logout')
# # @login_required
# # def logout():
# #     session.pop('logged_in', None)
# #     flash('Acabas de desloguearte!')
# #     return redirect(url_for('welcome'))




# if __name__ == '__main__':
#     app.run(debug=True, port=8000)