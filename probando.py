import tkinter
import tkinter as tk
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title("TITULO")
ventana.geometry("450x450")
ventana.config(bg="orange")
ventana.iconbitmap(r"C:\Users\AUTONOMA\Downloads\cosa.ico")


def mostrar_error():
    messagebox.showerror("Error", "!Solo numeros¡")



def sumar():
    numero1 =caja_texto1.get()
    numero2 = caja_texto2.get()

    if numero2.isnumeric() and numero1.isnumeric():
        caja3.config(text=f"{int(numero1)+int(numero2)}")
    else:
        messagebox.showerror("Error", "Debe colocar 2 números.")

def resta():
    numero1 =caja_texto1.get()
    numero2 =caja_texto2.get()

    if numero2.isnumeric() and numero1.isnumeric():
        caja3.config(text=f"{int(numero1)-int(numero2)}")
    else:
        messagebox.showerror("Error", "Debe colocar 2 números.")

def multiplicar():
    numero1 =caja_texto1.get()
    numero2 = caja_texto2.get()

    if numero2.isnumeric() and numero1.isnumeric():
        caja3.config(text=f"{int(numero1)*int(numero2)}")
    else:
        messagebox.showerror("Error", "Debe colocar 2 números.")

def Divicion():
    numero1 =caja_texto1.get()
    numero2 = caja_texto2.get()

    if numero2.isnumeric() and numero1.isnumeric():
        caja3.config(text=f"{int(numero1)/int(numero2)}")
    else:
        messagebox.showerror("Error", "Debe colocar 2 números.")

variable1=tkinter.StringVar()



caja3=tkinter.Label(ventana, text="RESULTADO", bg="white")



#CREACION DE LOS WIDGETS
titulo=tkinter.Label(ventana, text="Calculadora Simple", background="orange", foreground="red")
etiqueta1=tkinter.Label(ventana, text="Numero 1" , background="orange", foreground="red")
etiqueta2=tkinter.Label(ventana, text="Numero 2" , background="orange", foreground="red")
boton1=tkinter.Button(ventana, text="Suma", background="red", foreground="white", command=sumar)
boton2=tkinter.Button(ventana, text="Restar", background="red", foreground="white", command=resta)
boton3=tkinter.Button(ventana, text="Multiplicar", background="red" , foreground="white", command=multiplicar)
boton4=tkinter.Button(ventana, text="Dividir", background="red", foreground="white", command=Divicion)

caja_texto1=tkinter.Entry(ventana)
caja_texto2=tkinter.Entry(ventana)

#UBICACION DE LOS WIDGETS
titulo.grid(row=0, column=0, columnspan=2, pady=8)
titulo.config(font=("Arial", 15))
etiqueta1.grid(row=1, column=0, padx=10, pady=10)
etiqueta1.config(font=("Arial", 13))
etiqueta2.grid(row=2, column=0, padx=10, pady=10)
etiqueta2.config(font=("Arial", 13))
boton1.grid(row=3, column=0, columnspan=2, padx=0, pady=10)
boton1.config(font=("Arial", 10), pady=5, padx=60)
boton2.grid(row=4, column=0, columnspan=2, padx=0, pady=10)
boton2.config(font=("Arial", 10), pady=5, padx=60)
boton3.grid(row=5, column=0, columnspan=2, padx=0, pady=10)
boton3.config(font=("Arial", 10), pady=5, padx=50)
boton4.grid(row=6, column=0, columnspan=2, padx=0, pady=10)
boton4.config(font=("Arial", 10), pady=5, padx=60)
caja3.config(font=("Arial", 12))
caja_texto1.grid(row=1, column=1, padx=100, pady=10)
caja_texto2.grid(row=2, column=1, padx=100, pady=10)
caja3.grid(row=7, column=1, padx=100, pady=10)


ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)




ventana.mainloop()
 