from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=600, height=600)
miFrame.pack()


cuadroUsuario = Entry(miFrame)
cuadroUsuario.grid(row=0, column=1, padx=3, pady=3)
cuadroUsuario.config(fg="violet", justify="center")

textoNombre = Label(miFrame, text="Usuario: ")
textoNombre.grid(row=0, column=0)

#----------------------------------------------------

cuadroContraseña = Entry(miFrame)
cuadroContraseña.grid(row=1, column=1)
cuadroContraseña.config(show="*")


textoContraseña = Label(miFrame, text="Contraseña: ")
textoContraseña.grid(row=1, column=0)

#----------------------------------------------------

Button(miFrame, text="Enviar")
raiz.mainloop()