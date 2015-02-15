from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from passlib.hash import sha256_crypt
from project import db


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


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = sha256_crypt.encrypt(password)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<username: {}, email: {}'.format(self.username, self.email)