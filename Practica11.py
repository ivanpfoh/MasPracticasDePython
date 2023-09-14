#calcula el interes por año de un ahorro

cuenta_de_ahorros, primer_año, segundo_año, tercer_año = 0, 0, 0, 0
cuenta_de_ahorros = float(input('Ingrese la cantidad que tiene en la cuenta de ahorros:\n'))
primer_año = (round(((4/100)/12)*cuenta_de_ahorros, 2))+cuenta_de_ahorros
segundo_año = (round((((4/100)/12)*cuenta_de_ahorros)*2, 2))+primer_año
tercer_año = round((((4/100)/12)*cuenta_de_ahorros)*3, 2)+segundo_año
print('La cantidad de ahorros que tendra luego de intereses el primer año es de:', primer_año)
print('El segundo año sera de: ', segundo_año)
print('Y el tercer año sera de: ', tercer_año)
