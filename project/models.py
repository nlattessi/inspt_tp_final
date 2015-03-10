from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from passlib.hash import sha256_crypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager


class MenuCategoria(db.Model):

    __tablename__ = 'menu_categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    items = relationship('MenuItem', backref='categoria')
    
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<nombre: {}>'.format(self.nombre)


class MenuItem(db.Model):

    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    precio = db.Column(db.Numeric, nullable=True)
    categoria_id = db.Column(db.Integer, ForeignKey('menu_categorias.id'))

    def __init__(self, nombre, precio, categoria_id=None):
        self.nombre = nombre
        self.precio = precio
        self.categoria_id = categoria_id

    def __repr__(self):
        return '<nombre: {}, precio: >'.format(self.nombre, self.precio)


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)    
    password_hash = db.Column(db.String(128))

    '''def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    '''
    @property
    def password(self):
        raise AttributeError('password is not a readable atribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    '''
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    '''

    def __repr__(self):
        return '<username: {}, email: {}'.format(self.username, self.email)

@login_manager.user_loader
def load_user(user_id):
    #return User.query.filter_by(id=int(user_id)).first()
    return User.query.get(int(user_id))