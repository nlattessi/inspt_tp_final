import os
from app import create_app
from flask.ext.script import Manager
from app import db
from app.models import User, Categoria


app = create_app('default')
manager = Manager(app)


@manager.command
def adduser(username, admin=False):
    """Registrar un nuevo usuario."""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt="Confirmar: ")
    if password != password2:
        import sys
        sys.exit("Error: passwords no son iguales.")
    db.create_all()
    user = User(username=username, password=password, is_admin=admin)
    db.session.add(user)
    db.session.commit()
    print("Usuario {0} fue registrado con exito.".format(username))


@manager.command
def initdb():
    """Inicializa la db."""
    db.drop_all()
    db.create_all()
    categoria = Categoria(nombre="sin categoria", descripcion="categoria auxiliar para items sin categoria definida")
    db.session.add(categoria)

    user = User(username="admin", password="admin", is_admin=True)
    db.session.add(user)

    db.session.commit()
    print("Se inicializo la db. Se agrego la categoria auxiliar. Se creó el usuario admin")


if __name__ == '__main__':
    manager.run()