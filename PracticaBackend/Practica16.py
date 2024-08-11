from io import open

fichero = open('text to prove.txt', 'r')

texto = fichero.readlines()
contador = 0
contadorpalabras = 0
contadorletra = 0
for linea in texto:
    contador += 1
    for palabra in linea.split():
        contadorpalabras += 1
        for letra in palabra:
            contadorletra += 1

print("la cantidad de lineas que contiene el archivo es: ", contador)
print("La cantidad de palabras que contiene el archivo es de: ", contadorpalabras)
print("La cantidad de letras que contiene el archivo es de: ", contadorletra)

fichero.close()
