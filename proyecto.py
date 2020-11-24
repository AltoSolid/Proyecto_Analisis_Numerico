import tkinter as tk
from tkinter import *
from tkinter import ttk
#Métodos de Ecuaciones de una variable
from ecuaciones_una_variable.biseccion import biseccion
from ecuaciones_una_variable.reglafalsa import reglafalsa
from ecuaciones_una_variable.puntofijo import puntofijo
from ecuaciones_una_variable.newton import newton
from ecuaciones_una_variable.secante import secante_tabla
from ecuaciones_una_variable.raices_multiples import raicesMultiples
#Métodos de Sistemas de ecuaciones
from sistemas_de_ecuaciones.gauss import gauss
from sistemas_de_ecuaciones.gaussSeidel import gauss_seidel
from sistemas_de_ecuaciones.jacobi import jacobi
from sistemas_de_ecuaciones.pivoteoParcial import pivoteoParcial
from sistemas_de_ecuaciones.LUSimple import LUSimple
from sistemas_de_ecuaciones.Cholesky import Cholesky
from sistemas_de_ecuaciones.Crout import Crout
from sistemas_de_ecuaciones.Doolittle import Doolittle


def pintarBiseccion():
    ventanaBiseccion = tk.Toplevel(window)
    ventanaBiseccion.title("Bisection Method")
    labelTitulo = tk.Label(ventanaBiseccion, text="Bisection Method", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaBiseccion, text="Enter function", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaBiseccion)
    labelLimiteInferior = tk.Label(ventanaBiseccion, text="Enter lower limit", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaBiseccion)
    labelLimiteSuperior = tk.Label(ventanaBiseccion, text="Enter upper limit", fg="black", font=("Arial", 10))
    entradaB = ttk.Entry(ventanaBiseccion)
    labelTolerancia = tk.Label(ventanaBiseccion, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaBiseccion)
    espacio = tk.Label(ventanaBiseccion, text="")
    boton = tk.Button(ventanaBiseccion, text = "Calculate", command = lambda: llamarBiseccion(entradaFuncion.get(),entradaA.get(),entradaB.get(),entradaTolera.get(), ventanaBiseccion))
    
    labelTitulo.pack()
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelLimiteSuperior.pack()
    entradaB.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()
    
def llamarBiseccion(funcion, a, b, tolera, ventanaBiseccion):
    respuesta = biseccion(funcion, a, b, tolera)
    respuesta = "There is a root in: " + str(respuesta[0])
    labelRaiz = tk.Label(ventanaBiseccion, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    #labelTolerancia = tk.Label(ventanaBiseccion, text=respuesta[1], fg="black", font=("Arial", 10))
    #labelTolerancia.pack()
    
def pintarReglaFalsa():
    ventanaReglaFalsa = tk.Toplevel(window)
    ventanaReglaFalsa.title("False Position Method")
    labelTitulo = tk.Label(ventanaReglaFalsa, text="False Position Method", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaReglaFalsa, text="Enter function", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaReglaFalsa)
    labelLimiteInferior = tk.Label(ventanaReglaFalsa, text="Enter lower limit", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaReglaFalsa)
    labelLimiteSuperior = tk.Label(ventanaReglaFalsa, text="Enter upper limit", fg="black", font=("Arial", 10))
    entradaB = ttk.Entry(ventanaReglaFalsa)
    labelTolerancia = tk.Label(ventanaReglaFalsa, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaReglaFalsa)
    espacio = tk.Label(ventanaReglaFalsa, text="")
    boton = tk.Button(ventanaReglaFalsa, text = "Calculate", command = lambda: llamarReglaFalsa(entradaFuncion.get(),entradaA.get(),entradaB.get(),entradaTolera.get(), ventanaReglaFalsa))
    
    labelTitulo.pack()
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelLimiteSuperior.pack()
    entradaB.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()

def llamarReglaFalsa(funcion, a, b, tolera, ventanaReglaFalsa):
    respuesta = reglafalsa(funcion, a, b, tolera)
    respuesta = "There is a root in: " + str(respuesta)
    labelRaiz = tk.Label(ventanaReglaFalsa, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarPuntoFijo():
    ventanaPuntoFijo = tk.Toplevel(window)
    ventanaPuntoFijo.title("Fixed-Point Iteration Method")
    labelTitulo = tk.Label(ventanaPuntoFijo, text="Fixed-Point Iteration Method", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaPuntoFijo, text="Enter function", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaPuntoFijo)
    labelLimiteInferior = tk.Label(ventanaPuntoFijo, text="Enter lower limit", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaPuntoFijo)
    labelTolerancia = tk.Label(ventanaPuntoFijo, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaPuntoFijo)
    espacio = tk.Label(ventanaPuntoFijo, text="")
    boton = tk.Button(ventanaPuntoFijo, text = "Calculate", command = lambda: llamarPuntoFijo(entradaFuncion.get(),entradaA.get(), entradaTolera.get(), ventanaPuntoFijo))
    
    labelTitulo.pack()
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()

def llamarPuntoFijo(funcion, a, tolera, ventanaPuntoFijo):
    respuesta = puntofijo(funcion, a, tolera)
    respuesta = "There is a root in: " + str(respuesta)
    labelRaiz = tk.Label(ventanaPuntoFijo, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarNewton():
    ventanaNewton = tk.Toplevel(window)
    ventanaNewton.title("Newton Method")
    labelTitulo = tk.Label(ventanaNewton, text="Newton Method", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaNewton, text="Enter function", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaNewton)
    labelDFuncion = tk.Label(ventanaNewton, text="Enter function derivative", fg="black", font=("Arial", 10))
    entradaDFuncion = ttk.Entry(ventanaNewton)
    labelLimiteInferior = tk.Label(ventanaNewton, text="Enter lower limit", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaNewton)
    labelTolerancia = tk.Label(ventanaNewton, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaNewton)
    espacio = tk.Label(ventanaNewton, text="")
    boton = tk.Button(ventanaNewton, text = "Calculate", command = lambda: llamarNewton(entradaFuncion.get(), entradaDFuncion.get(), entradaA.get(), entradaTolera.get(), ventanaNewton))
    
    labelTitulo.pack()
    labelFuncion.pack()
    entradaFuncion.pack()
    labelDFuncion.pack()
    entradaDFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()
    
def llamarNewton(funcion, dfuncion, x0, tolera, ventanaNewton):
    respuesta = newton(funcion, dfuncion, x0, tolera)
    respuesta = "There is a root in: " + str(respuesta)
    labelRaiz = tk.Label(ventanaNewton, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarSecante():
    ventanaSecante = tk.Toplevel(window)
    ventanaSecante.title("Secant Methd")
    labelTitulo = tk.Label(ventana, text="Secant Methd", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaSecante, text="Enter function", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaSecante)
    labelLimiteInferior = tk.Label(ventanaSecante, text="Enter lower limit", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaSecante)
    labelTolerancia = tk.Label(ventanaSecante, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaSecante)
    espacio = tk.Label(ventanaSecante, text="")
    boton = tk.Button(ventanaSecante, text = "Calculate", command = lambda: llamarSecante(entradaFuncion.get(), entradaA.get(), entradaTolera.get(), ventanaSecante))
    
    labelTitulo.pack()
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()

def llamarSecante(funcion, xa, tolera, ventanaSecante):
    respuesta = secante_tabla(funcion, xa, tolera)
    respuesta = "There is a root in: " + str(respuesta)
    labelRaiz = tk.Label(ventanaSecante, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarRaicesMultiples():
    ventanaRaicesMultiples = tk.Toplevel(window)
    ventanaRaicesMultiples.title("Multiple Roots Method")
    labelTitulo = tk.Label(ventanaRaicesMultiples, text="Multiple Roots Method", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaRaicesMultiples, text="Enter function", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaRaicesMultiples)
    labelDf = tk.Label(ventanaRaicesMultiples, text="Enter first derivate", fg="black", font=("Arial", 10))
    entradaDf = ttk.Entry(ventanaRaicesMultiples)
    labelDDf = tk.Label(ventanaRaicesMultiples, text="Enter second derivate", fg="black", font=("Arial", 10))
    entradaDDf = ttk.Entry(ventanaRaicesMultiples)
    labelA = tk.Label(ventanaRaicesMultiples, text="Enter lower limit", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaRaicesMultiples)
    labelTolerancia = tk.Label(ventanaRaicesMultiples, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaRaicesMultiples)
    espacio = tk.Label(ventanaRaicesMultiples, text="")
    boton = tk.Button(ventanaRaicesMultiples, text = "Calculate", command = lambda: llamarRaicesMultiples(entradaFuncion.get(), entradaDf.get(), entradaDDf.get(), entradaA.get(), entradaTolera.get(), ventanaRaicesMultiples))
    
    labelTitulo.pack()
    labelFuncion.pack()
    entradaFuncion.pack()
    labelDf.pack()
    entradaDf.pack()
    labelDDf.pack()
    entradaDDf.pack()
    labelA.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()

def llamarRaicesMultiples(funcion, df, ddf, x0, tolera,ventanaRaicesMultiples):
    respuesta = raicesMultiples(funcion,df,ddf,x0,tolera)
    respuesta = "There is a root in : " + str(respuesta[0] )
    labelRaiz = tk.Label(ventanaRaicesMultiples, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
      
def pintarEliminacionGaussiana():
    ventanaEliminacionGauss = tk.Toplevel(window)
    ventanaEliminacionGauss.title("Gaussian Elimination Method")
    labelTitulo = tk.Label(ventanaEliminacionGaussian, text="Gaussian Elimination Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaEliminacionGauss, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaEliminacionGauss)
    espacio = tk.Label(ventanaEliminacionGauss, text="")
    boton = tk.Button(ventanaEliminacionGauss, text = "Calculate", command = lambda: llamarEliminacionGaussiana(entradaMatrizA.get(), ventanaEliminacionGauss))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    espacio.pack()
    boton.pack()

def llamarEliminacionGaussiana(matrizA, ventanaEliminacionGaussiana):
    respuesta = gauss(matrizA)
    labelMensaje = tk.Label(ventanaEliminacionGaussiana, text="The system solution is:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaEliminacionGaussiana, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarPivoteoParcial():
    ventanaPivoteoParcial = tk.Toplevel(window)
    ventanaPivoteoParcial.title("Partial Pivoting Method")
    labelTitulo = tk.Label(ventanaPivoteoParcial, text="Partial Pivoting Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaPivoteoParcial, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaPivoteoParcial)
    labelMatrizB = tk.Label(ventanaPivoteoParcial, text="Enter Matrix B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaPivoteoParcial)
    espacio = tk.Label(ventanaPivoteoParcial, text="")
    boton = tk.Button(ventanaPivoteoParcial, text = "Calculate", command = lambda: llamarPivoteoParcial(entradaMatrizA.get(), entradaMatrizB.get(), ventanaPivoteoParcial))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    espacio.pack()
    boton.pack()

def llamarPivoteoParcial(matrizA, matrizB, ventanaPivoteoParcial):
    respuesta = pivoteoParcial(matrizA, matrizB)
    labelMensaje = tk.Label(ventanaPivoteoParcial, text="The system solution is:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaPivoteoParcial, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarPivoteoTotal():
    pass

def llamarPivoteoTotal():
    pass
    
def pintarLU():
    ventanaLU = tk.Toplevel(window)
    ventanaLU.title("LU Gaussian Factorization Method")
    labelTitulo = tk.Label(ventanaLU, text="LU Gaussian Factorization Method", fg="black", font=("Arial", 15))
    labelMatrizAumentada = tk.Label(ventanaLU, text="Enter Augmented Matrix", fg="black", font=("Arial", 10))
    entradaMatrizAumentada = ttk.Entry(ventanaLU)
    espacio = tk.Label(ventanaLU, text="")
    boton = tk.Button(ventanaLU, text="Calculate", command = lambda: llamarLU(entradaMatrizAumentada.get(), ventanaLU))

    labelTitulo.pack()
    labelMatrizAumentada.pack()
    entradaMatrizAumentada.pack()
    espacio.pack()
    boton.pack()

def llamarLU(A, ventanaLU):
    respuesta = LUSimple(A)
    labelMensaje = tk.Label(ventanaLU, text="Solution:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaLU, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarCholesky():
    ventanaCholesky = tk.Toplevel(window)
    ventanaCholesky.title("Cholesky Factorization Method")
    labelTitulo = tk.Label(ventanaCholesky, text="Cholesky Factorization Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaCholesky, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaCholesky)
    labelMatrizB = tk.Label(ventanaCholesky, text="Enter Matrix B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaCholesky)
    labelN = tk.Label(ventanaCholesky, text="Enter value of n", fg="black", font=("Arial", 10))
    entradaN = ttk.Entry(ventanaCholesky)
    espacio = tk.Label(ventanaCholesky, text="")
    boton = tk.Button(ventanaCholesky, text = "Calculate", command = lambda: llamarCholesky(entradaMatrizA.get(), entradaMatrizB.get(), entradaN.get(), ventanaCholesky))

    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    labelN.pack()
    entradaN.pack()
    espacio.pack()
    boton.pack()    

def llamarCholesky(n, A, B, ventanaCholesky):
    respuesta = Cholesky(n, A, B)
    labelMensaje = tk.Label(ventanaCholesky, text="The solution to factoring is:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaCholesky, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarCrout():
    ventanaCrout = tk.Toplevel(window)
    ventanaCrout.title("Crout Factorization Method")
    labelTitulo = tk.Label(ventanaCrout, text="Crout Factorization Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaCrout, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaCrout)
    labelMatrizB = tk.Label(ventanaCrout, text="Enter Matrix B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaCrout)
    labelN = tk.Label(ventanaCrout, text="Enter value of n", fg="black", font=("Arial", 10))
    entradaN = ttk.Entry(ventanaCrout)
    espacio = tk.Label(ventanaCrout, text="")
    boton = tk.Button(ventanaCrout, text = "Calculate", command = lambda: llamarCrout(entradaMatrizA.get(), entradaMatrizB.get(), entradaN.get(), ventanaCrout))

    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    labelN.pack()
    entradaN.pack()
    espacio.pack()
    boton.pack()    

def llamarCrout(n, A, B, ventanaCrout):
    respuesta = Crout(n, A, B)
    labelMensaje = tk.Label(ventanaCrout, text="The solution to factoring is:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaCrout, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarDoolittle():
    ventanaDoolittle = tk.Toplevel(window)
    ventanaDoolittle.title("Doolittle Factorization Method")
    labelTitulo = tk.Label(ventanaDoolittle, text="Doolittle Factorization Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaDoolittle, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaDoolittle)
    labelMatrizB = tk.Label(ventanaDoolittle, text="Enter Matrix B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaDoolittle)
    labelN = tk.Label(ventanaDoolittle, text="Enter value of n", fg="black", font=("Arial", 10))
    entradaN = ttk.Entry(ventanaDoolittle)
    espacio = tk.Label(ventanaDoolittle, text="")
    boton = tk.Button(ventanaDoolittle, text = "Calculate", command = lambda: llamarDoolittle(entradaMatrizA.get(), entradaMatrizB.get(), entradaN.get(), ventanaDoolittle))

    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    labelN.pack()
    entradaN.pack()
    espacio.pack()
    boton.pack()   

def llamarDoolittle(n, A, B, ventanaDoolittle):
    respuesta = Doolittle(n, A, B)
    labelMensaje = tk.Label(ventanaDoolittle, text="The solution to factoring is:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaDoolittle, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarJacobi():
    ventanaJacobi = tk.Toplevel(window)
    ventanaJacobi.title("Jacobi Method")
    labelTitulo = tk.Label(ventanaJacobi, text="Jacobi Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaJacobi, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaJacobi)
    labelMatrizB = tk.Label(ventanaJacobi, text="Enter Matrix B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaJacobi)
    espacio = tk.Label(ventanaJacobi, text="")
    boton = tk.Button(ventanaJacobi, text = "Calculate", command = lambda: llamarJacobi(entradaMatrizA.get(), entradaMatrizB.get(), ventanaJacobi))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    espacio.pack()
    boton.pack()

def llamarJacobi(matrizA, matrizB, ventanaJacobi):
    respuesta = jacobi(matrizA, matrizB)
    labelMensaje = tk.Label(ventanaJacobi, text="The system solution is: ", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaJacobi, text=respuesta[0], fg="black", font=("Arial", 10))
    labelMensaje2 = tk.Label(ventanaJacobi, text="Error: ", fg="black", font=("Arial", 10))
    labelError = tk.Label(ventanaJacobi, text=respuesta[1], fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    labelMensaje2.pack()
    labelError.pack()
    
def pintarGaussSeidel():
    ventanaGaussSeidel = tk.Toplevel(window)
    ventanaGaussSeidel.title("Gauss Seidel Method")
    labelTitulo = tk.Label(ventanaGaussSeidel, text="Gauss Seidel Method", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaGaussSeidel, text="Enter Matrix A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaGaussSeidel)
    labelMatrizB = tk.Label(ventanaGaussSeidel, text="Enter Matrix B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaGaussSeidel)
    labelVector = tk.Label(ventanaGaussSeidel, text="Enter initial vector", fg="black", font=("Arial", 10))
    entradaVector = ttk.Entry(ventanaGaussSeidel)
    labelTolerancia = tk.Label(ventanaGaussSeidel, text="Enter tolerance", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaGaussSeidel)
    espacio = tk.Label(ventanaGaussSeidel, text="")
    boton = tk.Button(ventanaGaussSeidel, text = "Calculate", command = lambda: llamarGaussSeidel(entradaMatrizA.get(), entradaMatrizB.get(), entradaVector.get(), entradaTolera.get(),ventanaGaussSeidel))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    labelVector.pack()
    entradaVector.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    espacio.pack()
    boton.pack()

def llamarGaussSeidel(matrizA, matrizB, x0, tolera, ventanaGaussSeidel):
    respuesta = gauss_seidel(matrizA, matrizB, x0, tolera)
    labelMensaje = tk.Label(ventanaGaussSeidel, text="The system solution is:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaGaussSeidel, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarVandermonde():
    pass

def llamarVandermonde():
    pass
    
def pintarLagrange():
    pass

def llamarLagrange():
    pass
    
def pintarDiferenciasDivididas():
    pass

def llamarDiferenciasDivididas():
    pass
    

def metodoSeleccionado(event):
    seleccion = event.widget.get()
    if(seleccion == "Bisection"):
        pintarBiseccion()
    elif(seleccion == "Position Method"):
        pintarReglaFalsa()
    elif(seleccion == "Fixed-Point Iteration"):
        pintarPuntoFijo()
    elif(seleccion == "Newton"):
        pintarNewton()
    elif(seleccion == "Secant"):
        pintarSecante()
    elif(seleccion == "Multiple Roots"):
        pintarRaicesMultiples()
    elif(seleccion == "Gaussian Elimination"):
        pintarEliminacionGaussiana()
    elif(seleccion == "Partial Pivoting"):
        pintarPivoteoParcial()
    elif(seleccion == "Total Pivoting"):
        pintarPivoteoTotal()
    elif(seleccion == "LU"):
        pintarLU()
    elif(seleccion == "Cholesky"):
        pintarCholesky()
    elif(seleccion == "Crout"):
        pintarCrout()
    elif(seleccion == "Doolittle"):
        pintarDoolittle()
    elif(seleccion == "Jacobi"):
        pintarJacobi()
    elif(seleccion == "Gauss-Seidel"):
        pintarGaussSeidel()
    elif(seleccion == "Vandermonde"):
        pintarVandermonde()
    elif(seleccion == "Lagrange"):
        pintarLagrange()
    elif(seleccion == "divided differences(Newton)"):
        pintarDiferenciasDivididas()
    else: 
        print("No method was painted...")

window = Tk()

window.title("Numerical Methods")
window.geometry("500x280")
#window.state('zoomed')

titulo = tk.Label(window, text="Numerical Methods", fg="black", font=("Arial", 30))
titulo.config(anchor=CENTER)
titulo.pack()

tituloLista = tk.Label(window, text="Select a method", fg="black")
tituloLista.config(anchor=CENTER)
tituloLista.pack()

lista = ttk.Combobox(window, values=["Bisection", "Position Method", "Fixed-Point Iteration", "Newton", "Secant", "Multiple Roots", "Gaussian Elimination", "Partial Pivoting", "Total Pivoting", "LU", "Cholesky", "Crout", "Doolittle", "Jacobi", "Gauss-Seidel", "Vandermonde", "Lagrange", "divided differences(Newton)"])
lista.pack()
lista.current()
lista.bind("<<ComboboxSelected>>", metodoSeleccionado)

window.mainloop()
