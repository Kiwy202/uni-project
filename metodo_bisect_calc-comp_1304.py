#usando de referencia código de : https://www.kaggle.com/code/yaserrahmati/bisection-method?scriptVersionId=85328058&cellId=2
#https://colab.research.google.com/github/caam37830/book/blob/master/04_functions/roots.ipynb
import math 
import pandas as pd

# tolerancia de solución
tolerance = 0.001

# definición de solución
def f(x):
    return math.exp(-x) - x

# a y b iniciales
a = 0
b = 2

# inicializar contador
cnt = 0

# valor inicial de dx
dx = abs(b-a)

# Lista para almacenar los resultados de cada iteración
results = []

if f(a)*f(b) > 0:
    # f(a) y f(b) son del mismo signo
    print("No se encontró raíz")   
else:   
    # repetir hasta que dx < tolerancia
    while dx > tolerance:
        x = (a+b) / 2.0
        cnt += 1
        # tomo los valores de fa, fx y fa*fx para agregarlos a fila en pandas
        fa = f(a)
        fx = f(x)
        fa_fx = fa * fx
        
        # raíz en el lado izquierdo
        if fa_fx < 0:
            b_temp = b # valor temporal de b antes del cambio a x
            b = x
            results.append([cnt, a, b_temp, x, fa, fx, round(fa_fx, 5)])  # redondear a 5 decimales
        # raíz en el lado derecho
        else:
            a = x
            results.append([cnt, a, b, x, fa, fx, round(fa_fx, 5)])  # redondear a 5 decimales
        # actualizar la incertidumbre en la ubicación de la raíz
        dx = abs(b-a)  

# Convertir la lista de resultados en un DataFrame de pandas
df = pd.DataFrame(results, columns=["Iteración", "a", "b", "x", "f(a)", "f(x)", "f(a) * f(x)"])

# Agregar las columnas "cumple" al DataFrame
df["T"] = round((df["b"] - df["a"])/ 2 ** cnt,5) # validar
df["Cumple"] = df["f(a) * f(x)"].apply(lambda val: "si cumple" if val < 0.00001 else "no cumple") #con cero no detecta negativos con mas de 5 decimales por eso pongo 0.0000001

# Mostrar el resultado final
print("\nSe encontró la raíz f(x) = 0 con x =", x, "con una tolerancia de", tolerance)
print("\n*Tabla de resultados:\n")
# Mostrar el DataFrame con los resultados
df.head(cnt)