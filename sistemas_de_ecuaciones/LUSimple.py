import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
import numpy as np
#Crear clase para instanciar
#Pàrametro de entrada, matrix ampliada 


class LU_simple:

    def __init__(self,A):
        self.A = A 
        self.respuestaX = []
        self.respuestaz = []

    def sacarB(self,a):
        b = []
        for i in range(len(self.A)):
            b.append(self.A[i][len(self.A)-1])
        return b

    def crearListaUnos(self,n):
        l = []
        for i in range(n):
            l.append(1)
        return l

    def sustitucionRegresiva(self,a, b, n):
        variables = self.crearListaUnos(n)
        for i in range(n-1,-1,-1): 
            suma = 0
            for j in range(i+1,n):
                suma = suma + a[i][j]*variables[j]
            variables[i] = (b[i]-suma) / a[i][i]
        return variables

    def sustitucionProgresiva(self,a, b, n):
        variables = self.crearListaUnos(n)
        for i in range(n):
            suma = 0
            for j in range(i):
                suma = suma + a[i][j]*variables[j]
            variables[i] = (b[i]-suma) / a[i][i]
        return variables

    def comprobar_resultados(self,A,Y):
        suma = 0
        for p in range(len(self.A)):
            for t in range(len(self.A)-1):
                valor_matrizA = self.A[p][t]
                valor_matriY = Y[t]
                print()
                suma = suma + valor_matrizA*valor_matriY
            print(suma)
    
    def lu_simple(self):
        P, L, U = scipy.linalg.lu(self.A)
        # print ("A:")
        # pprint.pprint(self.A)
        # print(type(self.A))
        # print ("P:")
        # pprint.pprint(P)

        # print ("L:")
        # pprint.pprint(L)

        # print ("U:")
        # pprint.pprint(U)

        b = self.sacarB(self.A)
        Z = np.array(self.sustitucionProgresiva(U,b,len(U)))
        X = self.sustitucionRegresiva(U,Z,len(L))
        self.respuestaz = Z
        self.respuestaX = X
        # print("Z:",Z)
        # print("X:",X)
