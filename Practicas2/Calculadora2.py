

n1 = int(input("Ingrese el numero: "))
n2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion que va a realizar: ")

if operacion == "+":
    print(n1 + n2)
elif operacion == "/":
    print(int(n1/n2))
elif operacion == "-":
    print(n1 - n2)
elif operacion == "*":
    print(n1*n2)
elif operacion == "%":
    print(n1%n2)
elif operacion == "//":
    print(n1//n1)
else:
    print("Operacion no valida")