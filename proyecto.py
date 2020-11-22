import tkinter as tk
from tkinter import *
from tkinter import ttk
from ecuaciones_una_variable.biseccion import biseccion
from ecuaciones_una_variable.reglafalsa import reglafalsa
from ecuaciones_una_variable.puntofijo import puntofijo
from ecuaciones_una_variable.newton import newton
from ecuaciones_una_variable.secante import secante_tabla
from ecuaciones_una_variable.raices_multiples import raicesMultiples

from sistemas_de_ecuaciones.gauss import gauss
from sistemas_de_ecuaciones.gaussSeidel import gauss_seidel
from sistemas_de_ecuaciones.jacobi import jacobi
from sistemas_de_ecuaciones.pivoteoParcial import pivoteoParcial


def pintarBiseccion():
    ventanaBiseccion = tk.Toplevel(window)
    ventanaBiseccion.title("Método de Bisección")
    labelTitulo = tk.Label(ventanaBiseccion, text="Método de Bisección", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaBiseccion, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaBiseccion)
    labelLimiteInferior = tk.Label(ventanaBiseccion, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaBiseccion)
    labelLimiteSuperior = tk.Label(ventanaBiseccion, text="Ingrese el límite superior", fg="black", font=("Arial", 10))
    entradaB = ttk.Entry(ventanaBiseccion)
    labelTolerancia = tk.Label(ventanaBiseccion, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaBiseccion)
    espacio = tk.Label(ventanaBiseccion, text="")
    boton = tk.Button(ventanaBiseccion, text = "Calcular", command = lambda: llamarBiseccion(entradaFuncion.get(),entradaA.get(),entradaB.get(),entradaTolera.get(), ventanaBiseccion))
    
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
    respuesta = "Raíz en: " + str(respuesta[0])
    labelRaiz = tk.Label(ventanaBiseccion, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    #labelTolerancia = tk.Label(ventanaBiseccion, text=respuesta[1], fg="black", font=("Arial", 10))
    #labelTolerancia.pack()
    
def pintarReglaFalsa():
    ventanaReglaFalsa = tk.Toplevel(window)
    ventanaReglaFalsa.title("Método de Regla Falsa")
    labelTitulo = tk.Label(ventanaReglaFalsa, text="Método de Regla Falsa", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaReglaFalsa, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaReglaFalsa)
    labelLimiteInferior = tk.Label(ventanaReglaFalsa, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaReglaFalsa)
    labelLimiteSuperior = tk.Label(ventanaReglaFalsa, text="Ingrese el límite superior", fg="black", font=("Arial", 10))
    entradaB = ttk.Entry(ventanaReglaFalsa)
    labelTolerancia = tk.Label(ventanaReglaFalsa, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaReglaFalsa)
    espacio = tk.Label(ventanaReglaFalsa, text="")
    boton = tk.Button(ventanaReglaFalsa, text = "Calcular", command = lambda: llamarReglaFalsa(entradaFuncion.get(),entradaA.get(),entradaB.get(),entradaTolera.get(), ventanaReglaFalsa))
    
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
    respuesta = "Raíz en: " + str(respuesta)
    labelRaiz = tk.Label(ventanaReglaFalsa, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarPuntoFijo():
    ventanaPuntoFijo = tk.Toplevel(window)
    ventanaPuntoFijo.title("Método de Punto Fijo")
    labelTitulo = tk.Label(ventanaPuntoFijo, text="Método de Punto Fijo", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaPuntoFijo, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaPuntoFijo)
    labelLimiteInferior = tk.Label(ventanaPuntoFijo, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaPuntoFijo)
    labelTolerancia = tk.Label(ventanaPuntoFijo, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaPuntoFijo)
    espacio = tk.Label(ventanaPuntoFijo, text="")
    boton = tk.Button(ventanaPuntoFijo, text = "Calcular", command = lambda: llamarPuntoFijo(entradaFuncion.get(),entradaA.get(), entradaTolera.get(), ventanaPuntoFijo))
    
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
    respuesta = "Raíz en: " + str(respuesta)
    labelRaiz = tk.Label(ventanaPuntoFijo, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarNewton():
    ventanaNewton = tk.Toplevel(window)
    ventanaNewton.title("Método de Newton")
    labelTitulo = tk.Label(ventanaNewton, text="Método de Newton", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaNewton, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaNewton)
    labelDFuncion = tk.Label(ventanaNewton, text="Ingrese la derivada de la función", fg="black", font=("Arial", 10))
    entradaDFuncion = ttk.Entry(ventanaNewton)
    labelLimiteInferior = tk.Label(ventanaNewton, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaNewton)
    labelTolerancia = tk.Label(ventanaNewton, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaNewton)
    espacio = tk.Label(ventanaNewton, text="")
    boton = tk.Button(ventanaNewton, text = "Calcular", command = lambda: llamarNewton(entradaFuncion.get(), entradaDFuncion.get(), entradaA.get(), entradaTolera.get(), ventanaNewton))
    
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
    respuesta = "Raíz en: " + str(respuesta)
    labelRaiz = tk.Label(ventanaNewton, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarSecante():
    ventanaSecante = tk.Toplevel(window)
    ventanaSecante.title("Método de la Secante")
    labelTitulo = tk.Label(ventanaSecante, text="Método de la Secante", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaSecante, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaSecante)
    labelLimiteInferior = tk.Label(ventanaSecante, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaSecante)
    labelTolerancia = tk.Label(ventanaSecante, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaSecante)
    espacio = tk.Label(ventanaSecante, text="")
    boton = tk.Button(ventanaSecante, text = "Calcular", command = lambda: llamarSecante(entradaFuncion.get(), entradaA.get(), entradaTolera.get(), ventanaSecante))
    
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
    respuesta = "Raíz en: " + str(respuesta)
    labelRaiz = tk.Label(ventanaSecante, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarRaicesMultiples():
    ventanaRaicesMultiples = tk.Toplevel(window)
    ventanaRaicesMultiples.title("Método de Raices múltiples")
    labelTitulo = tk.Label(ventanaRaicesMultiples, text="Método de Raices múltiples", fg="black", font=("Arial", 15))
    labelFuncion = tk.Label(ventanaRaicesMultiples, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(ventanaRaicesMultiples)
    labelDf = tk.Label(ventanaRaicesMultiples, text="Ingrese la primera derivada", fg="black", font=("Arial", 10))
    entradaDf = ttk.Entry(ventanaRaicesMultiples)
    labelDDf = tk.Label(ventanaRaicesMultiples, text="Ingrese la segunda derivada", fg="black", font=("Arial", 10))
    entradaDDf = ttk.Entry(ventanaRaicesMultiples)
    labelA = tk.Label(ventanaRaicesMultiples, text="Ingrese la el limite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(ventanaRaicesMultiples)
    labelTolerancia = tk.Label(ventanaRaicesMultiples, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaRaicesMultiples)
    espacio = tk.Label(ventanaRaicesMultiples, text="")
    boton = tk.Button(ventanaRaicesMultiples, text = "Calcular", command = lambda: llamarRaicesMultiples(entradaFuncion.get(), entradaDf.get(), entradaDDf.get(), entradaA.get(), entradaTolera.get(), ventanaRaicesMultiples))
    
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
    respuesta = "Raiz en : " + str(respuesta[0] )
    labelRaiz = tk.Label(ventanaRaicesMultiples, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
    
def pintarEliminacionGaussiana():
    ventanaEliminacionGauss = tk.Toplevel(window)
    ventanaEliminacionGauss.title("Método de Eliminación Gaussiana")
    labelTitulo = tk.Label(ventanaEliminacionGauss, text="Método de Eliminación Gaussiana", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaEliminacionGauss, text="Ingrese la Matriz A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaEliminacionGauss)
    espacio = tk.Label(ventanaEliminacionGauss, text="")
    boton = tk.Button(ventanaEliminacionGauss, text = "Calcular", command = lambda: llamarEliminacionGaussiana(entradaMatrizA.get(), ventanaEliminacionGauss))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    espacio.pack()
    boton.pack()

def llamarEliminacionGaussiana(matrizA, ventanaEliminacionGaussiana):
    respuesta = gauss(matrizA)
    labelMensaje = tk.Label(ventanaEliminacionGaussiana, text="La solución del sistema es:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaEliminacionGaussiana, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarPivoteoParcial():
    ventanaPivoteoParcial = tk.Toplevel(window)
    ventanaPivoteoParcial.title("Método de Pivote Parcial")
    labelTitulo = tk.Label(ventanaPivoteoParcial, text="Método de Pivote Parcial", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaPivoteoParcial, text="Ingrese la Matriz A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaPivoteoParcial)
    labelMatrizB = tk.Label(ventanaPivoteoParcial, text="Ingrese la Matriz B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaPivoteoParcial)
    espacio = tk.Label(ventanaPivoteoParcial, text="")
    boton = tk.Button(ventanaPivoteoParcial, text = "Calcular", command = lambda: llamarPivoteoParcial(entradaMatrizA.get(), entradaMatrizB.get(), ventanaPivoteoParcial))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    espacio.pack()
    boton.pack()

def llamarPivoteoParcial(matrizA, matrizB, ventanaPivoteoParcial):
    respuesta = pivoteoParcial(matrizA, matrizB)
    labelMensaje = tk.Label(ventanaPivoteoParcial, text="La solución del sistema es:", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaPivoteoParcial, text=respuesta, fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    
def pintarPivoteoTotal():
    pass

def llamarPivoteoTotal():
    pass
    
def pintarLU():
    pass

def llamarLU():
    pass
    
def pintarCholesky():
    pass

def llamarCholesky():
    pass
    
def pintarCrout():
    pass

def llamarCrout():
    pass
    
def pintarDolittle():
    pass

def llamarDolittle():
    pass
    
def pintarJacobi():
    ventanaJacobi = tk.Toplevel(window)
    ventanaJacobi.title("Método de Jacobi")
    labelTitulo = tk.Label(ventanaJacobi, text="Método de Jacobi", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaJacobi, text="Ingrese la Matriz A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaJacobi)
    labelMatrizB = tk.Label(ventanaJacobi, text="Ingrese la Matriz B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaJacobi)
    espacio = tk.Label(ventanaJacobi, text="")
    boton = tk.Button(ventanaJacobi, text = "Calcular", command = lambda: llamarJacobi(entradaMatrizA.get(), entradaMatrizB.get(), ventanaJacobi))
    
    labelTitulo.pack()
    labelMatrizA.pack()
    entradaMatrizA.pack()
    labelMatrizB.pack()
    entradaMatrizB.pack()
    espacio.pack()
    boton.pack()

def llamarJacobi(matrizA, matrizB, ventanaJacobi):
    respuesta = jacobi(matrizA, matrizB)
    labelMensaje = tk.Label(ventanaJacobi, text="La solución del sistema es: ", fg="black", font=("Arial", 10))
    labelSolucion = tk.Label(ventanaJacobi, text=respuesta[0], fg="black", font=("Arial", 10))
    labelMensaje2 = tk.Label(ventanaJacobi, text="Con error de: ", fg="black", font=("Arial", 10))
    labelError = tk.Label(ventanaJacobi, text=respuesta[1], fg="black", font=("Arial", 10))
    labelMensaje.pack()
    labelSolucion.pack()
    labelMensaje2.pack()
    labelError.pack()
    
def pintarGaussSeidel():
    ventanaGaussSeidel = tk.Toplevel(window)
    ventanaGaussSeidel.title("Método de Gauss Seidel")
    labelTitulo = tk.Label(ventanaGaussSeidel, text="Método de Gauss Seidel", fg="black", font=("Arial", 15))
    labelMatrizA = tk.Label(ventanaGaussSeidel, text="Ingrese la Matriz A", fg="black", font=("Arial", 10))
    entradaMatrizA = ttk.Entry(ventanaGaussSeidel)
    labelMatrizB = tk.Label(ventanaGaussSeidel, text="Ingrese la Matriz B", fg="black", font=("Arial", 10))
    entradaMatrizB = ttk.Entry(ventanaGaussSeidel)
    labelVector = tk.Label(ventanaGaussSeidel, text="Ingrese el vector inicial", fg="black", font=("Arial", 10))
    entradaVector = ttk.Entry(ventanaGaussSeidel)
    labelTolerancia = tk.Label(ventanaGaussSeidel, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(ventanaGaussSeidel)
    espacio = tk.Label(ventanaGaussSeidel, text="")
    boton = tk.Button(ventanaGaussSeidel, text = "Calcular", command = lambda: llamarGaussSeidel(entradaMatrizA.get(), entradaMatrizB.get(), entradaVector.get(), entradaTolera.get(),ventanaGaussSeidel))
    
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
    labelMensaje = tk.Label(ventanaGaussSeidel, text="La solución del sistema es:", fg="black", font=("Arial", 10))
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
    
def pintarSplineLineal():
    pass

def llamarSplineLineal():
    pass

def pintarSplineCuadratico():
    pass

def llamarSplineCuadratico():
    pass

def pintarSplineCubico():
    pass

def llamarSplineCubico():
    pass

def metodoSeleccionado(event):
    seleccion = event.widget.get()
    if(seleccion == "Bisección"):
        pintarBiseccion()
    elif(seleccion == "Regla falsa"):
        pintarReglaFalsa()
    elif(seleccion == "Punto fijo"):
        pintarPuntoFijo()
    elif(seleccion == "Newton"):
        pintarNewton()
    elif(seleccion == "Secante"):
        pintarSecante()
    elif(seleccion == "Raices múltiples"):
        pintarRaicesMultiples()
    elif(seleccion == "Eliminación Gaussiana"):
        pintarEliminacionGaussiana()
    elif(seleccion == "Pivoteo parcial"):
        pintarPivoteoParcial()
    elif(seleccion == "Pivoteo total"):
        pintarPivoteoTotal()
    elif(seleccion == "LU"):
        pintarLU()
    elif(seleccion == "Cholesky"):
        pintarCholesky()
    elif(seleccion == "Crout"):
        pintarCrout()
    elif(seleccion == "Dolittle"):
        pintarDolittle()
    elif(seleccion == "Jacobi"):
        pintarJacobi()
    elif(seleccion == "Gauss-Seidel"):
        pintarGaussSeidel()
    elif(seleccion == "Vandermonde"):
        pintarVandermonde()
    elif(seleccion == "Lagrange"):
        pintarLagrange()
    elif(seleccion == "Diferencias divididas"):
        pintarDiferenciasDivididas()
    elif(seleccion == "Spline lineal"):
        pintarSplineLineal()
    elif(seleccion == "Spline cuadrático"):
        pintarSplineCuadratico()
    elif(seleccion == "Spline cúbico"):
        pintarSplineCubico()
    else: 
        print("No se pinto ningun metodo")

window = Tk()

window.title("Métodos Numéricos")
window.geometry("500x280")
#window.state('zoomed')

titulo = tk.Label(window, text="Métodos Numéricos", fg="black", font=("Arial", 30))
titulo.config(anchor=CENTER)
titulo.pack()

tituloLista = tk.Label(window, text="Seleccione un método", fg="black")
tituloLista.config(anchor=CENTER)
tituloLista.pack()

lista = ttk.Combobox(window, values=["Bisección", "Regla falsa", "Punto fijo", "Newton", "Secante", "Raices múltiples", "Eliminación Gaussiana", "Pivoteo parcial", "Pivoteo total", "LU", "Cholesky", "Crout", "Dolittle", "Jacobi", "Gauss-Seidel", "Vandermonde", "Lagrange", "Diferencias divididas", "Spline lineal", "Spline cuadrático", "Spline cúbico"])
lista.pack()
lista.current()
lista.bind("<<ComboboxSelected>>", metodoSeleccionado)

window.mainloop()
