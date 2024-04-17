#calcula las ganancias de una inversion dependiendo de la cantidad, años y procentaje anual.
inversion = float(input('Cuanto va a invertir?'))
interes_Anual = float(input('Cual es el interes anual?'))
años = int(input('cuantos años va a realizar las inversion?'))
print('El capital obtenido por la inversion es: ', str(round(cantidad * (interes / 100 + 1) ** años, 2)))