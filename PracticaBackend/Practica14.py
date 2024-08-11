cadena = "hola mundo"
frecuenciaLetras = {}
for letra in cadena:
    if letra in frecuenciaLetras:
        frecuenciaLetras[letra] += 1
    else:
        frecuenciaLetras[letra] = 1

print(frecuenciaLetras)