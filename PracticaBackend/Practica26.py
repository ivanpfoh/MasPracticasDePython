import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()
nombre = input("Ingrese el nombre que quiere consultar en la base de datos:\n> ")
cursor.execute("SELECT * FROM usuarios WHERE nombre = '{}'".format(nombre))
usuarios = cursor.fetchall()
print(usuarios)
conexion.commit()
conexion.close()