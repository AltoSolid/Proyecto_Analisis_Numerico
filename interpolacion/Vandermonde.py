#Hallar la matriz de Vandermonde
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Parametros de entrada 

class Vandermonde:

    def __init__(self,xi,fi):
        self.xi = xi
        self.fi = fi
        self.respuesta = ""

    def vandermonde(self):
        muestras = 101 #Tramos+1

        self.xi = np.array(self.xi)
        B = np.array(self.fi)
        n = len(self.xi)

        # Matriz Vandermonde
        D = np.zeros(shape=(n,n),dtype =float)
        for i in range(0,n,1):
            for j in range(0,n,1):
                potencia = (n-1)-j 
                D[i,j] = self.xi[i]**potencia

        # Resuelve sistema de ecuaciones AX=B
        coeficiente = np.linalg.solve(D,B)

        # Polinomio en forma simbólica
        x = sym.Symbol('x')
        polinomio = 0
        for i in range(0,n,1):
            potencia = (n-1)-i   
            termino = coeficiente[i]*(x**potencia)
            polinomio = polinomio + termino

        # Polinomio
        px = sym.lambdify(x,polinomio)

        # Para graficar el polinomio en [a,b]
        a = np.min(self.xi)
        b = np.max(self.xi)
        xin = np.linspace(a,b,muestras)
        yin = px(xin)

        self.respuesta = polinomio
        # Mostrar
        print('Matriz Vandermonde: ')
        print(D)
        print('Los coeficientes del polinomio: ')
        print(coeficiente)
        print('Polinomio de interpolación: ')
        print(polinomio)

        # Grafica
        plt.plot(self.xi,self.fi,'o', label='[xi,fi]')
        plt.plot(xin,yin, label='p(x)')
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.legend()
        plt.title(polinomio)
        plt.show()