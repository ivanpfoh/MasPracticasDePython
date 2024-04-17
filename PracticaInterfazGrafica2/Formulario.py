from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()


minombre = StringVar()
#----------------------------------------------------

cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="black", justify="center")

labelNombre = Label(miFrame, text="Nombre: ")
labelNombre.grid(row=0, column=0, sticky="W", pady=4)

#----------------------------------------------------

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)
cuadroApellido.config(fg="black", justify="center")

ApellidoLabel = Label(miFrame, text="Apellido: ")
ApellidoLabel.grid(row=1, column=0, sticky="w", pady=4)

#----------------------------------------------------

direccioncuadro = Entry(miFrame)
direccioncuadro.grid(row=2, column=1)
direccioncuadro.config(fg="black", justify="center")

direccionlabel = Label(miFrame, text="Direccion: ")
direccionlabel.grid(row=2, column=0,sticky="w", pady=4)

#----------------------------------------------------

cuadroTelefono = Entry(miFrame)
cuadroTelefono.grid(row=3, column=1)
cuadroTelefono.config(fg="black", justify="center")

cuadroTelefono = Label(miFrame, text="Telefono: ")
cuadroTelefono.grid(row=3, column=0, sticky="w", pady=4)

#----------------------------------------------------

cuadrodocumento = Entry(miFrame)
cuadrodocumento.grid(row=3, column=1)
cuadrodocumento.config(fg="black", justify="center")

cuadrodni = Label(miFrame, text="Numero de documento: ")
cuadrodni.grid(row=3, column=0, sticky="w", pady=4)

#----------------------------------------------------

textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=4, column=1)

scrollvert = Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollvert.set)

labelComentario = Label(miFrame, text="Comentarios: ")
labelComentario.grid(row=4,column=0, sticky="w")

#----------------------------------------------------
def codigoboton():
    minombre.set("ivan")

Button(miFrame, text="Enviar", command=codigoboton).grid(row=5, column=0)

Button(miFrame, text="Quit", command=miFrame.quit, justify="center",  padx=10, pady=4).grid(row=5, column=1, padx=5, pady=5)

raiz.mainloop()