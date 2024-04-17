#Calcula el indice de masa corporal del usuario
Peso = input('Ingrese su peso en KG: ')
Estatura = input('Ingrese su estatura en CM: ')
IMC = round(float(Peso)/float(Estatura)**2,2)
print('Tu indice de masa corporal es: ', IMC)