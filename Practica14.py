asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota = [0,0,0,0,0]
print("yo estudio: ", asignaturas[0:5])
nota[0] = int(input("que nota tienes en matematicas ")) 
nota[1] = int(input("que nota tienes en Fisica ")) 
nota[2] = int(input("que nota tienes en Quimica ")) 
nota[3] = int(input("que nota tienes en Historia ")) 
nota[4] = int(input("que nota tienes en Lengua "))

print("Mi nota en",asignaturas[0],"es", nota[0])
print("Mi nota en",asignaturas[1],"es", nota[1])
print("Mi nota en",asignaturas[2],"es", nota[2])
print("Mi nota en",asignaturas[3],"es", nota[3])
print("Mi nota en",asignaturas[4],"es", nota[4])