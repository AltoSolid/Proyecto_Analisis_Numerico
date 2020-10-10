import math 
from Functions import *

class PuntoFijo:
    def __init__(self):
        self.val = []
        self.raiz = " "
    

    def algoritmo(self, xi, Function, GFunction, iteraciones, tolerancia, tipo_error):
        #print(tipo_error)
        if(Function.evaluar(xi) == 0):
            self.raiz = f"{xi} es raíz"
        elif (iteraciones <= 0):
            self.raiz = "Iteraciones incorrectas ..."
        elif (tolerancia < 0):
            self.raiz = "Tolerancia incorrecta ..."
        else:
            xi_otro = xi
            cont = 1
            error = tolerancia+1
