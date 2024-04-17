import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

'''variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Autito", 50, "Juguetes"),
    ("Pelota", 35, "Deportes")
]'''
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


miCursor.execute("SELECT * FROM PRODUCTOS")

variableDatos = miCursor.fetchall()

print(variableDatos)


for producto in variableDatos:
    print("El producto:",producto[0], " tiene un valor de:",producto[1]," y se encuentra en la seccion de: ", producto[2])


miConexion.commit()


miConexion.close()