
numero = lambda numero: numero%2==0

numero = numero(int(input("Ingrese un numero:\n>")))

if numero == True:
    print("El numero es año bisiesto.")
else:
    print("El numero no es año bisiesto.")