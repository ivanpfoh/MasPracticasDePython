#Calcula el precio de un pan con el descuento adquirido

Precio_pan  = 3.49
pan_nodeldia = int(input('Cuantas barras de pan que no son del dia se vendieron?:\n'))
descuento = round((Precio_pan*60)/100, 2)
Precio_pan_final =  round(Precio_pan - descuento, 2)
print('la barra de pan sale habitualmente:', Precio_pan)
print('El descuento que se le hace por no ser fresca es de:', descuento)
print('El precio final es:', Precio_pan_final)