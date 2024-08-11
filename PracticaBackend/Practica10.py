numero = int(input("Ingrese un numero y se le devolvera su factorial:\n> "))
factorial = 0
for i in range(0, numero+1):
    factorial += numero*(numero-1)

print(factorial)