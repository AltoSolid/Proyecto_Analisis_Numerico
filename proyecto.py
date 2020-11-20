import tkinter as tk
from tkinter import *
from tkinter import ttk
from ecuaciones_una_variable.biseccion import biseccion
from ecuaciones_una_variable.reglafalsa import reglafalsa
from ecuaciones_una_variable.puntofijo import puntofijo
from ecuaciones_una_variable.newton import newton
from ecuaciones_una_variable.secante import secante_tabla

def pintarBiseccion():
    labelFuncion = tk.Label(window, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(window)
    labelLimiteInferior = tk.Label(window, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(window)
    labelLimiteSuperior = tk.Label(window, text="Ingrese el límite superior", fg="black", font=("Arial", 10))
    entradaB = ttk.Entry(window)
    labelTolerancia = tk.Label(window, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(window)
    boton = tk.Button(window, text = "Calcular", command = lambda: llamarBiseccion(entradaFuncion.get(),entradaA.get(),entradaB.get(),entradaTolera.get()))
    
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelLimiteSuperior.pack()
    entradaB.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    boton.pack()
    
def llamarBiseccion(funcion, a, b, tolera):
    respuesta = biseccion(funcion, a, b, tolera)
    labelRaiz = tk.Label(window, text=respuesta[0], fg="black", font=("Arial", 10))
    labelRaiz.pack()
    labelTolerancia = tk.Label(window, text=respuesta[1], fg="black", font=("Arial", 10))
    labelTolerancia.pack()
    
def pintarReglaFalsa():
    labelFuncion = tk.Label(window, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(window)
    labelLimiteInferior = tk.Label(window, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(window)
    labelLimiteSuperior = tk.Label(window, text="Ingrese el límite superior", fg="black", font=("Arial", 10))
    entradaB = ttk.Entry(window)
    labelTolerancia = tk.Label(window, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(window)
    boton = tk.Button(window, text = "Calcular", command = lambda: llamarReglaFalsa(entradaFuncion.get(),entradaA.get(),entradaB.get(),entradaTolera.get()))
    
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelLimiteSuperior.pack()
    entradaB.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    boton.pack()

def llamarReglaFalsa(funcion, a, b, tolera):
    respuesta = reglafalsa(funcion, a, b, tolera)
    labelRaiz = tk.Label(window, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarPuntoFijo():
    labelFuncion = tk.Label(window, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(window)
    labelLimiteInferior = tk.Label(window, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(window)
    labelTolerancia = tk.Label(window, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(window)
    boton = tk.Button(window, text = "Calcular", command = lambda: llamarPuntoFijo(entradaFuncion.get(),entradaA.get(), entradaTolera.get()))
    
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    boton.pack()

def llamarPuntoFijo(funcion, a, tolera):
    respuesta = puntofijo(funcion, a, tolera)
    labelRaiz = tk.Label(window, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarNewton():
    labelFuncion = tk.Label(window, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(window)
    labelDFuncion = tk.Label(window, text="Ingrese la derivada de la función", fg="black", font=("Arial", 10))
    entradaDFuncion = ttk.Entry(window)
    labelLimiteInferior = tk.Label(window, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(window)
    labelTolerancia = tk.Label(window, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(window)
    boton = tk.Button(window, text = "Calcular", command = lambda: llamarNewton(entradaFuncion.get(), entradaDFuncion.get(), entradaA.get(), entradaTolera.get()))
    
    labelFuncion.pack()
    entradaFuncion.pack()
    labelDFuncion.pack()
    entradaDFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    boton.pack()
    
def llamarNewton(funcion, dfuncion, x0, tolera):
    respuesta = newton(funcion, dfuncion, x0, tolera)
    labelRaiz = tk.Label(window, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarSecante():
    labelFuncion = tk.Label(window, text="Ingrese la función", fg="black", font=("Arial", 10))
    entradaFuncion = ttk.Entry(window)
    labelLimiteInferior = tk.Label(window, text="Ingrese el límite inferior", fg="black", font=("Arial", 10))
    entradaA = ttk.Entry(window)
    labelTolerancia = tk.Label(window, text="Ingrese la tolerancia", fg="black", font=("Arial", 10))
    entradaTolera = ttk.Entry(window)
    boton = tk.Button(window, text = "Calcular", command = lambda: llamarSecante(entradaFuncion.get(), entradaA.get(), entradaTolera.get()))
    
    labelFuncion.pack()
    entradaFuncion.pack()
    labelLimiteInferior.pack()
    entradaA.pack()
    labelTolerancia.pack()
    entradaTolera.pack()
    boton.pack()

def llamarSecante(funcion, xa, tolera):
    respuesta = secante_tabla(funcion, xa, tolera)
    labelRaiz = tk.Label(window, text=respuesta, fg="black", font=("Arial", 10))
    labelRaiz.pack()
    
def pintarRaicesMultiples():
    pass

def llamarRaicesMultiples():
    pass
    
def pintarEliminacionGaussiana():
    pass

def llamarEliminacionGaussiana():
    pass
    
def pintarPivoteoParcial():
    pass

def llamarPivoteoParcial():
    pass
    
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
    pass

def llamarJacobi():
    pass
    
def pintarGaussSeidel():
    pass

def llamarGaussSeidel():
    pass
    
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
window.state('zoomed')

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
