laberinto = [
    [':)', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]


for i in range(len(laberinto)):
    print(laberinto[i])



def posicionEnGrafica(laberinto):
    laberinto[movimientoUsuario[0]][movimientoUsuario[1]] = ":)"
    for i in range(len(laberinto)):
        print(laberinto[i])