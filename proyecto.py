import tkinter as tk
from tkinter import *
from tkinter import ttk
from ecuaciones_una_variable.biseccion import biseccion
from ecuaciones_una_variable.reglafalsa import reglafalsa
from ecuaciones_una_variable.puntofijo import puntofijo
from ecuaciones_una_variable.newton import newton
from ecuaciones_una_variable.secante import secante_tabla

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
