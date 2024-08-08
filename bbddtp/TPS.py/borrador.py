import sqlite3

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
platos = cursor.execute("SELECT nombre FROM plato WHERE categoria_id = 2")

def datos_a_texto(platos):
    texto = ""
    for plato in platos:
        texto += "\t".join(map(str, plato)) + "\n"
    print(texto)
    return texto

datos_a_texto(platos)

conexion.close()