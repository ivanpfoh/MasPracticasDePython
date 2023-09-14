#calcula el peso de un pedido de juguetes

peso_payasos = 112
peso_muñecas = 75

payasos_vendidos = int(input('¿Cual fue el numero de payasos vendidos?\n'))
muñecas_vendidas = int(input('¿Cual fue el numero de muñecas vendidas?\n'))
peso_total = (payasos_vendidos*peso_payasos)+(peso_muñecas*muñecas_vendidas)
print('El peso total del paquete que sera enviado es de: ', peso_total)