import numpy as np
import decimal

def puntofijo(funcion,a,tolera, iteramax = 40):
    gx = lambda x: eval(funcion)
    a = eval(a)
    tolera = eval(tolera)
    i = 1 # iteración
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tolera and i<=iteramax):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i+1
    respuesta = b
    # Validar respuesta
    if (i>=iteramax ):
       respuesta = np.nan
    return(respuesta)

# PROGRAMA ---------

# PROCEDIMIENTO
#respuesta = puntofijo("x**3+4*x**2-10",0,0.001)

# SALIDA
#print(respuesta)