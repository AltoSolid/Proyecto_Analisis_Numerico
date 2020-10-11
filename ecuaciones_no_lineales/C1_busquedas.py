#Este programa encuentra un intervalo en donde f(x) tiene cambio de signo (raiz)
#usando el metodo de busquedas incrementales

import math

print("Introduce la funcion:")
f = input()
print("Introduce el valor inicial:")
x = int(input())
print("¿Cual es tu delta?:")
d = input()
print("Introduce el numero de iteraciones:")
i = int(input())


def func():
    res = eval(f)
    return res
   
def fun1():
    res = eval(f)
    return res


name = "main"
if name == "main":
    if func() == 0:
        print(x,"es raiz")
    else:
        xa = x + d
        res1 = fun1()
        cont = 1 
        while (res1 * func() > 0)&(cont < i):
            x = xa
            res1 = func()
            xa = x + d
            res1 = fun1()
            cont = cont + 1
        if res1 == 0:
            print(xa,"es raiz")
        else:
            if (res1*func() < 0):
                print("[",x,",",xa,"]")
            else:
                print("El metodo falló, no se encuentra intervalo")