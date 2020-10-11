from Functions import *
import math


class Raices_Multiples:

    def __init__(self):
        self.valores = []
        self.raiz = ''

    def algoritmot(self, xi, function,iter, tol, err_type):

        try:
            Yi = function.evaluar(xi)
            d1F = function.derivarM(function,1,xi)
            d2F = function.derivarM(function,2,xi)
            if(Yi == 0):
                self.raiz = f"{xi} solución"
            elif(iter<=0):
                self.raiz = "valor invalido de iteracion"
            elif(tol<0):
                self.raiz = "limite invalido de toleracia"
            else:
                error = tol+1000000
                counter = 1
                xi_1 = xi
                Yi_1 = Yi
                self.valores.append([counter, xi, '%E' %Yi, '%E' %d1F, '%E' %d2F, '%E' %error])

                while(Yi!=0 and error>=tol and counter<=iter):
                    xi = float(xi_1 - Yi_1*d1F/(d1F**2 - Yi_1*d2F))                                           
                    Yi = function.evaluar(xi)
                    # Error A
                    if(err_type):
                        error = math.fabs(xi-xi_1)           # #Usando usar math.fabs(x) se puede generar un error cuando x es complejo
                    # Error R
                    else:
                        error = math.fabs((xi-xi_1)/xi)      # #Usando usar math.fabs(x) se puede generar un error cuando x es complejo
                        print("Absolute error")
                    
                    d1F = function.derivarM(function,1,xi)
                    d2F = function.derivarM(function,2,xi)
                    counter+=1
                    self.valores.append([counter,'%f' %xi, '%E' %Yi, '%E' %d1F, '%E' %d2F, '%E' %error])
                    Yi_1 = Yi
                    xi_1 = xi


                if(Yi == 0):
                    self.raiz = f"{xi} Raiz"
                elif(error<=tol):
                    self.raiz = f"{xi} es aproximación a raiz"
                else:
                    self.raiz = "Número iteraciones excedido"
                    
        except Exception as e:
            print(e)
            self.raiz = "Error"



    
    def value_table(self):
        return self.valores
    def get_sol(self):
        return str(self.raiz)