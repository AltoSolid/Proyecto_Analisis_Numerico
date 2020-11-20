# Algoritmo de Bisección
# [a,b] se escogen de la gráfica de la función
# error = tolera

import numpy as np
import matplotlib.pyplot as plt

# INGRESO DE VARIABLES

def biseccion(funcion,a, b, tolera=0.001):
    fx = lambda x: eval(funcion)
    a = eval(a)
    b = eval(b)
    tolera = eval(tolera)
    #a = int(a)
    #b = int(b)
    # fx = lambda x: x*3 + 4*x*2 - 10 

    # PROCEDIMIENTO
    tramo = b-a
    while not(tramo<tolera):
        c = (a+b)/2
        fa = fx(a)
        fb = fx(b)
        fc = fx(c)
        cambia = np.sign(fa)*np.sign(fc)
        if cambia < 0: 
            a = a
            b = c
        if cambia > 0:
            a = c
            b = b
        tramo = b-a

    # SALIDA
    #print('       raiz en: ', c)
    #print('error en tramo: ', tramo)
    return (c,tramo)

#biseccion("x*3 + 4*x*2 - 10" ,"1","2")