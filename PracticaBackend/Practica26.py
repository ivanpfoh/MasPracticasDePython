import sqlite3

conexion = sqlite3.connect('ejemplo.db', 'r')

cursor = conexion.cursor()



conexion.commit()
conexion.close()