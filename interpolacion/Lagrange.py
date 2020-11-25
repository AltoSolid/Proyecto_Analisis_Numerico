#Polinomio interpolante de Lagrange
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Datos de prueba

class Lagrange:

    def __init__(self,xi,fi):
        self.xi = xi
        self.fi = fi
        self.respuesta = ""
    
    def lagrange(self):
        n = len(self.xi)
        x = sym.Symbol('x')
        polinomio = 0
        divisorL = np.zeros(n, dtype = float)
        for i in range(0,n,1):
            # Termino de Lagrange
            numerador = 1
            denominador = 1
            for j  in range(0,n,1):
                if (j!=i):
                    numerador = numerador*(x-self.xi[j])
                    denominador = denominador*(self.xi[i]-self.xi[j])
            terminoLi = numerador/denominador
            polinomio = polinomio + terminoLi*self.fi[i]
            divisorL[i] = denominador
        # simplifica el polinomio
        polisimple = polinomio.expand()
        # para evaluación numérica
        px = sym.lambdify(x,polisimple)

        # Puntos para la gráfica
        muestras = 101
        a = np.min(self.xi)
        b = np.max(self.xi)
        pxi = np.linspace(a,b,muestras)
        pfi = px(pxi)
        self.respuesta = polisimple
        # Salida
        print('Valores de fi: ',self.fi)
        print('Divisores en L(i): ',divisorL)
        print()
        print('Polinomio de Lagrange, expresiones')
        print(polinomio)
        print()
        print('Polinomio de Lagrange: ')
        print(polisimple)

        # Gráfica
        plt.plot(self.xi,self.fi,'o', label = 'Puntos')
        plt.plot(pxi,pfi, label = 'Polinomio')
        plt.legend()
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.title('Interpolación Lagrange')
        plt.show()