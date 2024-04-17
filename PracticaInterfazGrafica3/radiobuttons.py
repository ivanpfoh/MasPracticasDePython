from tkinter import *

root = Tk()


varOpcion = IntVar()
varCheck = IntVar()

def imprimir():
    print(varOpcion.get())

    if varOpcion.get()==1:
        etiqueta.config(text="has elegido masculino")
    else:
        etiqueta.config(text="has elegido femenino")

Label(root, text="Género:").pack()


Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()


Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()


Checkbutton(root, text="Check In").pack()
Checkbutton(root, text="Check Out").pack()


root.mainloop()