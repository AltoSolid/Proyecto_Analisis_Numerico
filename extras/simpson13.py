import numpy as np
import matplotlib.pyplot as plt

    #fx = lambda x: np.sqrt(x)*np.sin(x)
    # intervalo de integración
    #a = 1
    #b = 3
    #tramos = 8

def simpson1_3(funcion, a, b, tramos):
    fx = lambda x: eval(funcion)
    a = eval(a)
    b = eval(b)
    tramos = eval(tramos)

    # Regla de Simpson 1/3
    h = (b-a)/tramos
    xi = a
    area = 0
    for i in range(0,tramos,2):
        deltaA = (h/3)*(fx(xi)+4*fx(xi+h)+fx(xi+2*h))
        area = area + deltaA
        xi = xi + 2*h
    respuesta = "Integral is: " + str(area)
    return respuesta

#simpson1_3("np.sqrt(x)*np.sin(x)","1","3","8")