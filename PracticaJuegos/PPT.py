

Piedra, Papel , Tijera = 1 ,2 ,3

def ppt():
    Eleccion_Jugador1 = int(input("Jugador 1: Ingrese su eleccion [1 -> Piedra ],[2 -> Papel],[3 -> Tijera]"))
    Eleccion_Jugador2 = int(input("Jugador 2: Ingrese su eleccion [1 -> Piedra ],[2 -> Papel],[3 -> Tijera]"))
    if Eleccion_Jugador1 == 1 and Eleccion_Jugador2 == 2:
        print("Gana el Jugador 2 !!!")
    elif Eleccion_Jugador1 == 1 and Eleccion_Jugador2 == 3:
        print("Gana el Jugador 1 !!!")
    elif Eleccion_Jugador1 == 1 and Eleccion_Jugador2 == 1:
        print("Empate!!!")
    
    
    
    if Eleccion_Jugador1 == 2 and Eleccion_Jugador2 == 1:
        print("Gana el Jugador 1 !!!")
    elif Eleccion_Jugador1 == 2 and Eleccion_Jugador2 == 3:
        print("Gana el Jugador 2 !!!")
    elif Eleccion_Jugador1 == 2 and Eleccion_Jugador2 == 2:
        print("Empate!!!")
    
    
    if Eleccion_Jugador1 == 3 and Eleccion_Jugador2 == 1:
        print("Gana el Jugador 2 !!!")
    elif Eleccion_Jugador1 == 3 and Eleccion_Jugador2 == 2:
        print("Gana el Jugador 1 !!!")
    elif Eleccion_Jugador1 == 3 and Eleccion_Jugador2 == 3:
        print("Empate!!!")
        



ppt()