from io import open

fichero = open("fichero.txt","r")

texto = fichero.read()

fichero.close()

print(texto)