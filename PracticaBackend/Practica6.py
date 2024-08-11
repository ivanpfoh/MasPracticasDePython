numero = int(input("Ingrese un numero para saber su tabla:\n> "))
for i in range(1,numero+1):
        print("{}*{}= ".format(numero, i), numero*i)