palabra = "computadora"
plabrapalindromo = "salas"

def palindromo(palabra1):
    return palabra1[::-1] == palabra1


print(palindromo(palabra))