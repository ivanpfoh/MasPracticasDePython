import random
numero = random.randrange(50)
while True:
    numero_ingresado = int(input("Adivine el numero entre 1 y 50: "))
    if numero_ingresado == numero:
        print("Correcto! Felicitaciones!")
        break
    elif numero_ingresado > numero:
        print("Un poco mas abajo!")
    elif numero_ingresado < numero:
        print("Un poco mas arriba")
    else:
        continue