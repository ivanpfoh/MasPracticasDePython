respuesta = str(input("Ingrese si quiere utilizar la tabla de multiplicar con S para aceptar o N para negar: " ))
while respuesta == ("S") or ("s"):
    numero = int(input("Ingrese el numero del que quiere su tabla de multiplicar: "))
    if numero > 0:
        for i in range(1, 11):
            print(f"{numero} x {i} = ", numero*i)
    elif numero < 0:
        print("Ingrese un numero positivo.")
        continue
    else:
        break

