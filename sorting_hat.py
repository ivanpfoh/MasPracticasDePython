Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin  = 0

respuesta = int(input(print("Do you like 1.Dawn or 2.Dusk?")))
if respuesta == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif respuesta == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("entrada incorrecta")


respuesta2 = int(input(print("When I’m dead, I want people to remember me as:1)The Good 2)The Great 3)The Wise 4)The Bold")))  
if respuesta2 == 1:
    Hufflepuff = Hufflepuff + 2
elif respuesta2 == 2:
    Slytherin = Slytherin + 2
elif respuesta2 == 3:
    Ravenclaw = Ravenclaw + 2   
elif respuesta2 == 4:
    Gryffindor = Gryffindor + 2
else:
    print("entrada incorrecta")


respuesta3 =  int(input(print("Which kind of instrument most pleases your ear? 1)The Violin 2)The Trumpet 3)The Piano 4)The Drum")))
if respuesta2 == 2:
    Hufflepuff = Hufflepuff + 4
elif respuesta2 == 1:
    Slytherin = Slytherin + 4
elif respuesta2 == 3:
    Ravenclaw = Ravenclaw + 4
elif respuesta2 == 4:
    Gryffindor = Gryffindor + 4
else:
    print("entrada incorrecta")

if (Gryffindor>Slytherin) and (Gryffindor>Hufflepuff) and (Gryffindor>Ravenclaw):
    print("The house winner is Gryffindor con",Gryffindor, "puntos")
elif (Ravenclaw>Slytherin) and (Ravenclaw>Hufflepuff) and (Gryffindor<Ravenclaw):
    print("The house winner is Ravenclaw con",Ravenclaw, "puntos")
elif (Ravenclaw<Slytherin) and (Slytherin>Hufflepuff) and (Gryffindor<Slytherin):
    print("The house winner is Slytherin con",Slytherin, "puntos")
else:
    print("The house winner is Hufflepuff con",Hufflepuff, "puntos")