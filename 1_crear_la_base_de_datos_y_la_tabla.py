import sqlite3

con = sqlite3.connect('inventario.db')

cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad >= 0),
    precio REAL NOT NULL CHECK (precio >= 0)
) ''')

con.close()