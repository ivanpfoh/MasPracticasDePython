import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

cursor.execute("INSERT INTO usuarios VALUES "\
    "(1, 'ivan pfoh', 'ivansdfdsf@fdsfsdf.com')")

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchone()
print(usuarios)

conexion.commit()
conexion.close()