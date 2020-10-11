#Este programa halla la solucion a la ecuacion f(x)=0 en el intervalo [a,b]
#usando el metodo de la biseccion. 

import math

print("Ingrese el limite inferiror del intervalo:")
a = float(input())
print("Ingrese el intervalo superior del intervalo:")
b = float(input())
print("Ingrese la funcion:")
f = input()
print("Ingrese el numero de iteraciones:")
i = input()
print("Ingrese la tolerancia:")
tol = input()

def fun1():
	ya = eval(f)
	return ya

def fun2():
        yb = eval(f)
        return yb

def funm():
        yc = eval(f)
        return yc


if __name__=="__main__":
        if fun1 == 0:
                print(a,"es raiz")
        else:
                if fun2==0:
                        print(b,"es raiz")
                else:
                        if (fun1()*fun2())>0:
                                print("Intervalo invalido")
                        else:
                                c = (a+b)/2
                                funm()
                                error = tol + 1
                                cont = 1
                                while (funm()!= 0)&(error>tol)&(cont<i):
                                        if (fun1()*funm())<0:
                                                b = c
                                                fun2()
                                                
                                        else:
                                                a = c
                                                fun1()
                                        
                                        xaux = c
                                        xaux = ((a+b)/2)
                                        funm()
                                        error = abs(c-xaux)
                                        cont = cont + 1
                                if funm() == 0:
                                        print(c,"es raiz")
                                else:
                                        if error <= tol:
                                                print(c,"es raiz con un error igual a:",error)
                                        else:
                                                print("El metodo falló")
                                