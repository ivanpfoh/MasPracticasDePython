from io import open
try:
    fichero = open("textasd", "r")
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error con la lectura del archivo, no existe. Error =>", type(e).__name__)