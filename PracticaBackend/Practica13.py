Notas = {"ivan pfoh":10, "santos claudia":8, "carlos":7, "maria":5}
mejorcalificacion = 0
for nota in Notas:
    if Notas[nota] > mejorcalificacion:
        mejorcalificacion = Notas[nota]
    else:
        pass

print(mejorcalificacion)