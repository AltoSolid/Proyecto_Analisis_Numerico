# Método de Newton-Raphson
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)

import numpy as np

def newton(funcion, dfuncion, x0, tolera):
    # INGRESO
    fx = lambda x: eval(funcion)
    dfx = lambda x: eval(dfuncion)
    x0 = eval(x0)
    tolera = eval(tolera)
    # PROCEDIMIENTO
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo>=tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,tramo])
        xi = xnuevo

    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    n=len(tabla)

    # SALIDA
    # print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    return xi
    # print(tabla)
    #print('raiz en: ', xi)
    #print('con error de: ',tramo)

#newton("x**3 + 4*x**2 - 10", "3*x**2 + 8*x",2,0.001 )