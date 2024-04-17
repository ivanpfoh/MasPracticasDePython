from tkinter import *
raiz = Tk()

raiz.title("Horoscopo")

#raiz.resizable(1, 1)#el primero es width, y el seungo es height de la ventana
#raiz.iconbitmap("PracticaInterfazGrafica/logo canal yotube.ico")

#raiz.geometry("650x350")



raiz.config(bg="black")
raiz.config(relief="groove")
raiz.config(bd=35)
miFrame = Frame()
miFrame.pack(fill=X, expand="True")
miFrame.config(width="650", height="350")
miFrame.config(bg="white")#background
miFrame.config(bd=35)#pone el grosor del borde 
miFrame.config(relief="groove")#borde especial llamado groove
miFrame.config(cursor="hand2")


cuadrtoTexto = Entry(raiz)
cuadrtoTexto.pack()

raiz.mainloop() #esta instruccion siempre en el final