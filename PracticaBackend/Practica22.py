from fractions import Fraction

def inverso(n1):
    try:
        print(Fraction(1, n1))
    except ZeroDivisionError:
        print("No se puede dividir por 0, Ingrese otro numero valido.")

inverso(0)