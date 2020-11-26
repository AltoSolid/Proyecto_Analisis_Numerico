import numpy as np

def simpson_3_8(funcion, a,b,tramos):
    
    f = lambda x: eval(funcion)
    a = eval(a)
    b = eval(b)
    tramos = eval(tramos)
    h = (b - a) / tramos
    
    area = f(a) + f(b)
    
    for i in range(1,tramos):
        k = a + i*h
        
        if i%2 == 0:
            area = area + 2 * f(k)
        else:
            area = area + 3 * f(k)
    
    area = area * 3 * h / 8
    #print(area)
    respuesta = "Integral is: " + str(area)
    return respuesta

#simpson_3_8("np.sqrt(x)*np.sin(x)","1","3","9")