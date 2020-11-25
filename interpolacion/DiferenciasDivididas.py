# Polinomio interpolante usando el metodo de
# Diferencias Divididas de Newton
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Datos de prueba

class Diferencias_divididas:
    def __init__(self,xi,fi):
        self.xi = xi
        self.fi = fi
        self.respuesta = ""
    
    def diferencias_divididas(self):
        '''
        Ingesar el vector de los valores de x
        Ingresar el vector de y
        '''

                # Tabla de Diferencias Divididas Avanzadas
        titulo = ['i   ','xi  ','fi  ']
        n = len(self.xi)
        ki = np.arange(0,n,1)
        tabla = np.concatenate(([ki],[self.xi],[self.fi]),axis=0)
        tabla = np.transpose(tabla)
        # Diferencias divididas vacia
        dfinita = np.zeros(shape=(n,n),dtype=float)
        tabla = np.concatenate((tabla,dfinita), axis=1)
        # Calcula tabla, inicia en columna 3
        [n,m] = np.shape(tabla)
        diagonal = n-1
        j = 3
        while (j < m):
            # Añade título para cada columna
            titulo.append('F['+str(j-2)+']')
            # cada fila de columna
            i = 0
            paso = j-2 # inicia en 1
            while (i < diagonal):
                denominador = (self.xi[i+paso]-self.xi[i])
                numerador = tabla[i+1,j-1]-tabla[i,j-1]
                tabla[i,j] = numerador/denominador
                i = i+1
            diagonal = diagonal - 1
            j = j+1

        # POLINOMIO con diferencias Divididas
        # caso: puntos equidistantes en eje x
        dDividida = tabla[0,3:]
        n = len(dfinita)
        # expresión del polinomio con Sympy
        x = sym.Symbol('x')
        polinomio = self.fi[0]
        for j in range(1,n,1):
            factor = dDividida[j-1]
            termino = 1
            for k in range(0,j,1):
                termino = termino*(x-self.xi[k])
            polinomio = polinomio + termino*factor
        # simplifica multiplicando entre (x-xi)
        polisimple = polinomio.expand()

        # polinomio para evaluacion numérica
        px = sym.lambdify(x,polisimple)

        # Puntos para la gráfica
        muestras = 101
        a = np.min(self.xi)
        b = np.max(self.xi)
        pxi = np.linspace(a,b,muestras)
        pfi = px(pxi)
        self.respuesta= polisimple
        # SALIDA
        
        np.set_printoptions(precision = 4)
        print('Tabla Diferencia Dividida')
        print([titulo])
        print(tabla)
        print('dDividida: ')
        print(dDividida)
        print('polinomio: ')
        print(polinomio)
        print('polinomio simplificado: ' )
        print(polisimple)

        # Gráfica
        plt.plot(self.xi,self.fi,'o', label = 'Puntos')
        plt.plot(pxi,pfi, label = 'Polinomio')
        plt.legend()
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.title(str(polisimple))
        plt.show()



