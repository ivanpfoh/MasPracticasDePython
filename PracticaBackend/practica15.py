traducciones = {"hola":'hello',"adios":'bye', "ahora":'now', "como":'how'}

def diccionario(palabra):
    return traducciones[palabra]

print("La palabra Significa: ",diccionario(input("Ingrese la palabra que quiere saber en ingles:\n> ")))