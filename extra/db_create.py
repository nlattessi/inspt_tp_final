from project import db
from project.models import MenuItem, MenuCategoria, User

# Creo la base y las tablas
db.create_all()

# Inserto datos
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(MenuCategoria("categoria de test"))
db.session.add(MenuItem("item de test", 1, 1))
#db.session.add(MenuCategoria("hamburgesas"))
#db.session.add(MenuCategoria("ensaladas"))
#db.session.add(MenuItem("hamburgesa con queso", 30))
#db.session.add(MenuItem("ensalada caprese", 45.50))

# Commiteo los cambios
db.session.commit()

user = User.query.filter_by(username='admin').first()
print(user)

#import sqlite3

#with sqlite3.connect("database.db") as connection:
#    c = connection.cursor()
#    c.execute("UPDATE menu_items SET categoria_id = 1 WHERE id = 1")
#    c.execute("UPDATE menu_items SET categoria_id = 2 WHERE id = 2")