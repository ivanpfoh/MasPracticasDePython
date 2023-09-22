
datos = {}
datos = {"nombre_completo":"Ivan Pfoh" ,"numero_de_documento":"(ej)43333333", "fecha_de_nacimiento":"10/03/2001", "ciudad":"rada tilly", "Actualidad":"estudiando analisis de sistemas" , "lenguaje" : "python"}

Mi_tupla = ()
Mi_tupla = ("ivan", "pfoh")
print(datos["nombre_completo"])

mi_lista = []

def juego_favorito():
    k, p, respuesta, contador = "", 0, "", 0
    p = int(input("cuantos juegos favoritos tiene \n "))
    while contador <= p:        
        respuesta = ""
        juego = str(input("Tiene un juego favorito \n "))
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        n = 0
        juego = str(input("Ingrese su juego favorito \n "))
        mi_lista.insert(n+1,juego)
        n += 1
        contador += 1
        
    

juego_favorito()
print(mi_lista)


