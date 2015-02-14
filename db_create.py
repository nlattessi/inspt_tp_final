from app import db
from models import MenuItem, MenuCategoria

# Creo la base y las tablas
db.create_all()


# Inserto datos
db.session.add(MenuCategoria("hamburgesas"))
db.session.add(MenuCategoria("ensaladas"))
db.session.add(MenuItem("hamburgesa con queso", 30))
db.session.add(MenuItem("ensalada caprese", 45.50))

# Commiteo los cambios
db.session.commit()


import sqlite3

with sqlite3.connect("database.db") as connection:
    c = connection.cursor()
    c.execute("UPDATE menu_items SET categoria_id = 1 WHERE id = 1")
    c.execute("UPDATE menu_items SET categoria_id = 2 WHERE id = 2")