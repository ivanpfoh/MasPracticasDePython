#este programa te dice tu horoscopo
#solucionar que entre al bucle de elif si o si

print("Ingrese su dia de nacimiento")
dia = int(input())
print("Ingrese su mes de nacimiento")
mes = int(input())

"""
Aries: 21 de marzo al 19 de abril
Tauro: 20 de abril y al 20 de mayo
Géminis: 21 de mayo al 20 de junio
Cáncer: 21 de junio al 22 de julio
Leo: 23 de julio al 22 de agosto
Virgo: 23 de agosto al 22 de septiembre
Libra: 23 de septiembre al 22 de octubre
Escorpio: 23 de octubre al 21 de noviembre
Sagitario: 22 de noviembre al 21 de diciembre
Capricornio: 22 de diciembre al 19 de enero
Acuario: 20 de enero al 18 de febrero
Piscis: 19 de febrero al 20 de marzo
"""

if mes < 0 and dia < 0:
    print("Ingrese un numero valido, de 1 a 31")
elif mes == 1 and dia <= 19:
    print("Su signo zodiacal es:")
    print("capricornio")
elif mes == 2 and dia <= 18:
    print("Su signo zodiacal es:")
    print("Acuario")
elif mes == 3 and dia <= 20:
    print("Su signo zodiacal es:")
    print("piscis")
elif mes == 4 and dia <= 19:
    print("Su signo zodiacal es:")
    print("aries")
elif mes == 5 and dia <= 20:
    print("Su signo zodiacal es:")
    print("tauro")
elif mes == 6 and dia <= 20:
    print("Su signo zodiacal es:")
    print("geminis")
elif mes == 7 and dia <= 22:
    print("Su signo zodiacal es:")
    print("cancer")
elif mes == 8 and dia <= 22:
    print("Su signo zodiacal es:")
    print("leo")
elif mes == 9 and dia <= 22:
    print("Su signo zodiacal es:")
    print("virgo")
elif mes == 10 and dia <= 22:
    print("Su signo zodiacal es:")
    print("libra")
elif mes == 11 and dia <= 21:
    print("Su signo zodiacal es:")
    print("escorpio")
elif mes == 12 and dia <= 21:
    print("Su signo zodiacal es:")
    print("sagitario")
elif mes == 1 and dia >= 20:
    print("Su signo zodiacal es:")
    print("acuario")
elif mes == 2 and dia >= 21:
    print("Su signo zodiacal es:")
    print("piscis")
elif mes == 3 and dia >= 21:
    print("Su signo zodiacal es:")
    print("aries")
elif mes == 4 and dia >= 20:
    print("Su signo zodiacal es:")
    print("tauro")
elif mes == 5 and dia >= 21:
    print("Su signo zodiacal es:")
    print("geminis")
elif mes == 6 and dia >= 21:
    print("Su signo zodiacal es:")
    print("cancer")
elif mes == 7 and dia >= 23:
    print("Su signo zodiacal es:")
    print("leo")
elif mes == 8 and dia >= 23:
    print("Su signo zodiacal es:")
    print("virgo")
elif mes == 9 and dia >= 23:
    print("Su signo zodiacal es:")
    print("libra")
elif mes == 10 and dia >= 23:
    print("Su signo zodiacal es:")
    print("escorpio")
elif mes == 11 and dia >= 22:
    print("Su signo zodiacal es:")
    print("sagitario")
elif mes == 12 and dia >= 22:
    print("Su signo zodiacal es:")
    print("capricornio")