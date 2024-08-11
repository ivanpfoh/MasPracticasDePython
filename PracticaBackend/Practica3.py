try:
    numero = int(input("Ingrese un numero:\n> "))

    if numero % 2== 0:
        print("El numero {} es par".format(numero))
    elif numero == 0:
        print("El numero {} es 0".format(numero))
    else:
        print("El numero {} es impar".format(numero))
except:
    print("Valor ingresado no valido.")