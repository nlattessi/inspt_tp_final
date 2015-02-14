import sqlite3

with sqlite3.connect("sample.db") as connecton:
    c = connecton.cursor()
    c.execute("DROP TABLE menu_items")
    c.execute("CREATE TABLE menu_items(nombre TEXT, precio INTEGER)")
    c.execute('INSERT INTO menu_items VALUES("hamburgesa con queso", 30)')
    c.execute('INSERT INTO menu_items VALUES("ensalada caprese", 45.50)')