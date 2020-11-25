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
    
    #f(a) * f(b) < 0 ; Converge     
    if (a == b):
        error1 = " [{0} , {1}] It isn't an interval".format(a,b)
        return error1

    if ((fx(a) * fx(b)) >= 0):
        error2 = "The method doesn't converge with the interval [{0} , {1}]. f({0}) * f({1}) > 0".format(a,b)
        return error2
    
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
    raiz = "There is a root in: {0}".format(c)

    # SALIDA
    return raiz
    
    #print("Raiz {0}".format(raiz))

#reglafalsa("x**3 + 4*x**2 - 10" ,1,2)