
height = int(input("Ingrese su altura "))
credits = int(input("Ingrese la cantidad de creditos que tiene "))

if height >= 137 and credits >= 10:
    print("disfrute su viaje")
elif height < 137:
        print("No eres lo suficientemente alto para montar")
elif credits < 10:
    print("No tiene suficientes creditos")
else:
     print("Datos no validos")
