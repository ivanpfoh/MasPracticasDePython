import sqlite3

conexion = sqlite3.connect("MiDatabase.db")
cursor = conexion.cursor()
teclados1 = [('Razer blackwidow',13, 200000),
            ('Logitech prodigy',14, 155000),
            ('Hyperx', 16, 233333)]

cursor.executemany("INSERT INTO teclados VALUES (?,?,?)", teclados1)
conexion.commit()
conexion.close()