# Método de la secante
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)

import numpy as np

def secante_tabla(funcion,xa,tolera):
    fx = lambda x: eval(funcion)
    xa = eval(xa)
    tolera = eval(tolera)
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    n = len(tabla)
    return(tabla[n-1,2])

# PROGRAMA ####################
# INGRESO
"""fx = lambda x: x*3 + 4*x*2 - 10

a = 1 ; b = 2
xa = 1.5
tolera = 0.001
tramos = 100"""

# PROCEDIMIENTO
#tabla = secante_tabla("x**3 + 4*x**2 - 10",xa,0.001)
# n = len(tabla)
# raiz = tabla[n-1,2]

#raiz = tabla

# SALIDA
# np.set_printoptions(precision=4)
# print('[xa ,\t xb , \t xc , \t tramo]')
# for i in range(0,n,1):
#     print(tabla[i])
#print('raiz en: ', raiz)