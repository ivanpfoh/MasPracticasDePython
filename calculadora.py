#comentario recordatorio para decir que todo anda perfecto, solo tuve errores de tipeo y no dejaban funionar bien el codigo

"""
comentario de tres lineas 
para probar
y tener en cuenta todos los metodos de comentarios en python
"""

numero1, numero2, resultado = 0, 0, 0
operacion = ""
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: ')) 
operacion = str(input('ingrese la operacion que desea realizar: '))
if operacion == "suma":
    resultado = numero1 + numero2
elif operacion == "resta":
    resultado = numero1 - numero2
elif operacion == "multiplicacion":
    resultado = numero1 * numero2
elif operacion == "division":
    resultado = numero1 / numero2
elif operacion == "mod":
    resultado = numero1 % numero2
print('El resultado es: ', resultado)