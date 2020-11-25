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

    #f(a) * f(b) < 0 ; Converge     
    if (a == b):
        error1 = " [{0} , {1}] No es un intervalo".format(a,b)
        return error1

    if ((fx(a) * fx(b)) >= 0):
        error2 = "El método no converge con el intervalo [{0} , {1}]. f({0}) * f({1}) > 0".format(a,b)
        return error2

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
    raiz = "There is a root in: {0}".format(c)

    # SALIDA
    #print('       raiz en: ', c)
    #print('error en tramo: ', tramo)
    # tramo -> es el error
    
    return raiz



#biseccion("x*3 + 4*x*2 - 10" ,"1","2")