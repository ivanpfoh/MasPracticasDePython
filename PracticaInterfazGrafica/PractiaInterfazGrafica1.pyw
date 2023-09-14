from tkinter import *
raiz = Tk()

raiz.title("Horoscopo")

#raiz.resizable(1, 1)#el primero es width, y el seungo es height de la ventana

raiz.iconbitmap("PracticaInterfazGrafica/logo canal yotube.ico")

#raiz.geometry("650x350")

raiz.config(bg="red")

miFrame = Frame()
miFrame.pack()
miFrame.config(width="650", height="350")
miFrame.config(bg="white")#background
miFrame.config(bd=35)#pone el grosor del borde
miFrame.config(relief="groove")#borde especial llamado groove


raiz.mainloop() #esta instruccion siempre en el final