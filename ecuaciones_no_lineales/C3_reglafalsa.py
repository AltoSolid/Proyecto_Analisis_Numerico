#Este programa halla la solucion a la ecuacion f(x)=0 en el intervalo [a,b]
#usando el metodo de la regla falsa

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
        ypm = eval(f)
        return ypm

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
                                pm = (fun2*a-fun1*b)/(fun2-fun1)
                                funm()
                                error = tol + 1
                                cont = 1
                                while (funm()!=0)&(error>tol)&(cont<i):
                                     if (fun1()*funm())<0:
                                                a = pm
                                                fun2() 
                                                
                                     else:
                                                b = pm
                                                fun1()
                                     pmAux = pm
                                     pmAux = (fun2*a-fun1*b)/(fun2-fun1)
                                     funm()
                                     error = abs(pm-pmAux)
                                     cont = cont + 1
                                if funm() == 0:
                                    print(pm, "es raiz")
                                else: 
                                    if error <= tol:
                                        print(pm, "es raiz con un error igual a", error)
                                    else:
                                        print("El metodo falló")

       
