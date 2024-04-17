import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()



miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
        )''')

miCursor.execute('''
    CREATE TABLE MARCAS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_MARCAS VARCHAR(50),
        PRECIO_PROMEDIO INTEGER,
        SECCION VARCHAR(20)
        )''')

marcas = [
    ("Toyota", 1000, "autos"),
    ("Ford", 1000, "camionetas"),
    ("Volvo", 9000, "camiones"),
    ("BMW", 1000, "autos"),
    ("Mustang", 25500, "autos")
]


productos=[
    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("pelota", 45, "ceramica")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
miCursor.executemany("INSERT INTO MARCAS VALUES (NULL,?,?,?)", marcas)


#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'Tren', 15, 'jugueteria')")

miConexion.commit()

miConexion.close()