import numpy as np
import matplotlib.pyplot as plt


def trapecio (funcion, a, b, tramos):
    fx = lambda x: eval(funcion)
    a = eval(a)
    b = eval(b)
    tramos = eval(tramos)
    # Usando tramos equidistantes en intervalo
    h = (b-a)/tramos
    xi = a
    suma = fx(xi)
    for i in range(0,tramos-1,1):
        xi = xi + h
        suma = suma + 2*fx(xi)
    suma = suma + fx(b)
    area = h*(suma/2)
    respuesta = "Integral is: " + str(area)
    return respuesta

# trapecio("np.sqrt(x)*np.sin(x)","1", "3","4")