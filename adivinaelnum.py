import random


numero_random = random.randint(1,10)

while True:
    numero_ingresado = int(input("Ingrese un numero entre 1 y 10: "))
    if numero_ingresado == numero_random:
        print("Bien hecho! Lo encontraste!")
        break
    else:
        print("Incorrecto! Prueba otra vez!")
        