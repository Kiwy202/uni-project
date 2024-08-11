import tkinter
import tkinter as tk

ventana = tkinter.Tk()
ventana.title ("suma de numeros")
ventana.geometry("400x400")

#Funciones
def sumar():
    primero=int(caja1.get())
    segundo=int(caja2.get())
    sumar=(primero+segundo)
    return variable1.set(sumar)

variable1=tkinter.StringVar()

etiqueta1=tkinter.Label(ventana, text="suma de numeros")
caja1=tkinter.Entry(ventana, text="primer número")
caja2=tkinter.Entry(ventana, text="segundo número")
boton1=tkinter.Button(ventana, text="adicion", command=sumar)
caja3=tkinter.Entry(ventana,textvariable=variable1)

etiqueta1.pack()
caja1.pack()
caja2.pack()
boton1.pack()
caja3.pack()
ventana.mainloop()