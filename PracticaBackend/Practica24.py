import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

cursor.execute("CREATE TABLE usuarios"\
            "(id INTEGER, nombre VARCHAR (50), correo VARCAHAR (50))")

conexion.commit()
conexion.close()