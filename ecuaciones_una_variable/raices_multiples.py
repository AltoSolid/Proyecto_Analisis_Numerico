
def raicesMultiples(f,dx,ddx,x0,tol=0.001,t_error=1):
    x0 = eval(x0)
    tol = eval(tol)
    resultados = [] #matriz para guardar resultados
    y0 = evaluador(f,x0)
    dx0 = evaluador(dx,x0) #primera derivada
    ddx0 = evaluador(ddx,x0) #segunda derivada
    cont = 0
    error = (tol/1.0) + 1
    den = dx0**2-y0*ddx0
    resultados.append([cont,x0,y0,dx0,ddx0,den,error])
    while y0 != 0 and error > tol and dx0 != 0 and ddx0 != 0 and den != 0 and cont < 17:
        xn = x0 - (y0*dx0)/den
        y0 =  evaluador(f,xn)
        dx0 = evaluador(dx,xn)
        ddx0 = evaluador(ddx,xn)

        if t_error == 1:
            error = abs(xn - x0)
        else:
            error= abs((xn-x0)/xn)
        x0 = xn
        cont += 1
        den = dx0**2-y0*ddx0
        resultados.append([cont,x0,y0,dx0,ddx0,den,error])
    #imprimir(['Iteración','xn','f(xn)',"f'(xi)","f''(xn)",'den','Error'],resultados)
    if y0 == 0:
        print (x0, " Es una raiz")
    elif error <= tol:
        print (x0, " Es aproximacion a una raiz con una tolerancia = ",tol)
    elif dx0 == 0:
        print (x0, " Es una posible raiz multiple")
    elif ddx0 == 0:
        print (x0, " Es una posible raiz multiple")
    elif den == 0:
        print ("El denominador se hizo 0")
    #elif cont > niter:
        #print ("Fracaso el numero de iteraciones")
    return (x0,tol)

def evaluador(funcion, x):
    valor = {"x":x}
    result = eval(funcion,{},valor)
    return result

#evaluador("3*x*2+3*x*3-2*x",1)
#raicesMultiples("x**3+4*x**2 -10","3*x**2+8*x","6*x+8",1)