from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class MenuItem(db.Model):

    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    precio = db.Column(db.Integer, nullable=True)
    categoria_id = db.Column(db.Integer, ForeignKey('menu_categorias.id'))

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return '<nombre: {}, precio: >'.format(self.nombre, self.precio)


class MenuCategoria(db.Model):

    __tablename__ = 'menu_categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    items = relationship('MenuItem', backref='categoria')
    
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<nombre: {}>'.format(self.nombre)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __repr__(self):
        return '<nombre: {}, email: {}'.format(self.nombre, self.email)