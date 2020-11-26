
import numpy as np

def raicesMultiples(funcion,dfuncion,ddfuncion,x0,tol,t_error=1):
    f =  lambda x: eval((funcion))
    dx =  lambda x: eval((dfuncion))
    ddx =  lambda x: eval((ddfuncion))
    x0 = eval(x0)
    tol = eval(tol)
    resultados = [] #matriz para guardar resultados
    y0 = f(x0)
    dx0 = dx(x0) #primera derivada
    ddx0 = ddx(x0) #segunda derivada
    # print("yo:",y0)
    # print("dxo:",dx0)
    # print("ddxo:",ddx0)
    cont = 0
    error = (tol/1.0) + 1
    den = dx0 ** 2 - y0 * ddx0
    resultados.append([cont,x0,y0,dx0,ddx0,den,error])
    while y0 != 0 and error > tol and dx0 != 0 and ddx0 != 0 and den != 0 and cont < 17:
        xn = x0 - (y0*dx0)/den
        y0 =  f(xn)
        dx0 = dx(xn)
        ddx0 = ddx(xn)

        if t_error == 1:
            error = abs(xn - x0)
        else:
            error= abs((xn-x0)/xn)
        x0 = xn
        cont += 1
        den = dx0**2-y0*ddx0
        resultados.append([cont,x0,y0,dx0,ddx0,den,error])
    #imprimir(['Iteración','xn','f(xn)',"f'(xi)","f''(xn)",'den','Error'],resultados)
    # if y0 == 0:
    #     print (x0, " It's a root")
    # elif error <= tol:
    #     print (x0, " It's approximation to a root with a tolerance = ",tol)
    # elif dx0 == 0:
    #     print (x0, " It's a possible multiple root")
    # elif ddx0 == 0:
    #     print (x0, " It's a possible multiple root")
    # elif den == 0:
    #     print ("The denominator was made 0")
    # #elif cont > niter:
    #     #print ("Fracaso el numero de iteraciones")
    # print(x0)
    return (x0,tol)

# def evaluador(funcion, x):
#     # print("******************")
#     # funcion = eval(funcion)
#     # print(type(funcion))
#     # print(type(x))
#     valor = {"x":x}

#     result = eval(funcion,{},valor)
#     #result = (funcion(x))
#     #result = lambda x: eval(funcion,{},valor)
#     #print(result)
#     #print(funcion(x))
#     return result

#evaluador("3*x*2+3*x*3-2*x",1)
#raicesMultiples("x**3+4*x**2 -10","3*x**2+8*x","6*x+8","1","0.0001")
#raicesMultiples("np.exp(-x)-x","-np.exp(-x)-1","np.exp(-x)","0","0.001")
