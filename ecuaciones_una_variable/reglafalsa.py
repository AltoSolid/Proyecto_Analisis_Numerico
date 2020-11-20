# Algoritmo Posicion Falsa para raices
# busca en intervalo [a,b]
import numpy as np

# INGRESO

def reglafalsa(funcion,a, b, tolera=0.001):
    fx = lambda x: eval(funcion)
    a = eval(a)
    b = eval(b)
    tolera = eval(tolera)
    # PROCEDIMIENTO
    tramo = abs(b-a)
    while not(tramo<=tolera):
        fa = fx(a)
        fb = fx(b)
        c = b - fb*(a-b)/(fa-fb)
        fc = fx(c)
        cambia = np.sign(fa)*np.sign(fc)
        if (cambia > 0):
            tramo = abs(c-a)
            a=c
        else:
            tramo = abs(b-c)
            b=c
    raiz = c

    # SALIDA
    return c
    #print("Raiz {0}".format(raiz))

#reglafalsa("x**3 + 4*x**2 - 10" ,1,2)