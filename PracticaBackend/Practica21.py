numero1 = float(input("Ingrese el primer numero para dividir: "))
numero2 = float(input("Ingrese el segundo numero para dividir: "))

try:
    print("El resultado de la division entre {} y {} es de: ".format(numero1, numero2), numero1/numero2)
except ZeroDivisionError:
        print("No se puede dividir por 0, Ingrese otro numero valido.")