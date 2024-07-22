



"""Created by Ivan Pfoh"""


laberinto = [
    [':)', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
posicionEnLaberinto = (0,0)
movimientoUsuario = (0,0)
fila = 0
columna = 0


print("BIENVENIDO AL LABERINTO, TE MOVERAS POR EL MISMO DANDO PASOS DE UNO EN UNO, ESTOS SON LOS COMANDO SPARA MOVERTE POR EL LABERINTO: avanzar_arriba,avanzar_abajo,avanzar_izquierda,avanzar_derecha")
print("Que empiece el juego!")

for i in range(len(laberinto)):
    print(laberinto[i])

def avanzar_abajo():
    global fila
    global columna
    fila += 1
    global posicionEnLaberinto 
    posicionEnLaberinto = (fila, columna)
    
    
def avanzar_arriba():
    global fila
    global columna
    fila -= 1
    global posicionEnLaberinto 
    posicionEnLaberinto = (fila, columna)
    

def avanzar_izquierda():
    global fila
    global columna
    columna -= 1
    global posicionEnLaberinto 
    posicionEnLaberinto = (fila, columna)
    

def avanzar_derecha():
    global fila
    global columna
    columna += 1
    global posicionEnLaberinto 
    posicionEnLaberinto = (fila, columna)
    

funciones_permitidas = {
    "avanzar_abajo": avanzar_abajo,
    "avanzar_arriba": avanzar_arriba,
    "avanzar_izquierda": avanzar_izquierda,
    "avanzar_derecha": avanzar_derecha
}

def posicionEnGrafica(laberinto):
    laberinto[movimientoUsuario[0], movimientoUsuario[1]] = ":)"
    for i in range(len(laberinto)):
        print(laberinto[i])
        
while (posicionEnLaberinto != (4, 4)) & (posicionEnLaberinto not in muro):

    movimientoUsuario = input("Ingrese el movimiento que quiere realizar: [avanzar_arriba,avanzar_abajo,avanzar_izquierda,avanzar_derecha] \n")
    posicionEnGrafica(laberinto)
    if movimientoUsuario in funciones_permitidas:
        funciones_permitidas[movimientoUsuario]()

    


if posicionEnLaberinto == (4,4):
    print("Lograste escapar del laberinto! Felicitaciones!")
else:
    print("Oh no! Te has chocado con un muro, vuleve a intentarlo!")