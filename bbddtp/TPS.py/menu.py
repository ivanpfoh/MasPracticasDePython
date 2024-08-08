from tkinter import *
import sqlite3
#------------------Conexion DB--------

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

primeros = cursor.execute("SELECT nombre FROM plato WHERE categoria_id = 1").fetchall()
segundos = cursor.execute("SELECT nombre FROM plato WHERE categoria_id = 2").fetchall()
postres = cursor.execute("SELECT nombre FROM plato WHERE categoria_id = 3").fetchall()


def datos_a_texto(n):
    texto = ""
    for i in n:
        texto += "\t".join(map(str, i)) + "\n"
    return texto

primeros = datos_a_texto(primeros)
segundos = datos_a_texto(segundos)
postres = datos_a_texto(postres)
#----------------------Raiz-----------

root = Tk()
root.config(bg="grey")

#-----------------------Frame---------

frame = Frame(root)
frame.pack()
frame.config(bg="grey", relief="ridge", bd=15)

#-----------------------Menu----------


#-----Primeros
label1 = Label(frame,text = "Primeros")
label1.pack(anchor=CENTER)
label1.config(padx=4,pady=4, background="dark grey", font=("Comic Sans MS", 12), borderwidth=3)
label2 = Label(frame,text = primeros)
label2.pack(anchor=CENTER)
label2.config(background="light grey", font=("Comic Sans MS", 12))

#-----Segundos
label3 = Label(frame,text= "Segundos")
label3.pack(anchor=CENTER)
label3.config(padx=4,pady=4, background="dark grey", font=("Comic Sans MS", 12), borderwidth=3)
label4 = Label(frame,text = segundos)
label4.pack(anchor=CENTER)
label4.config(background="light grey", font=("Comic Sans MS", 12))

#-----Postres
label5 = Label(frame,text= "Postres")
label5.pack(anchor=CENTER)
label5.config(padx=4,pady=4, background="dark grey", font=("Comic Sans MS", 12), borderwidth=3)
label6 = Label(frame,text = postres)
label6.pack(anchor=CENTER)
label6.config(background="light grey", font=("Comic Sans MS", 12))

#-----------------------------------
conexion.close()
root.mainloop()