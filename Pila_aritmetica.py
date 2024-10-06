"""
Escriba un programa que evalúe, con la ayuda de una pila, una expresión aritmética dada en notación posfija/prefija
"""

class Pila:
    def __init__(self):
        self.items = []
    
    def apilador(self, item):
        self.items.append(item)
    
    def desapilador(self):
        return self.items.pop() if self.items else None

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    for elemento in expresion.split():  
        if elemento.isdigit():
            pila.apilador(int(elemento))
        else:
            op2 = pila.desapilador()
            op1 = pila.desapilador()
            if elemento == '+':
                pila.apilador(op1 + op2)
            elif elemento == '-':
                pila.apilador(op1 - op2)
            elif elemento == '*':
                pila.apilador(op1 * op2)
            elif elemento == '/':
                pila.apilador(op1 / op2)
    return pila.desapilador()

expresion = input("Expresión en notación posfija: ")
resultado = evaluar_expresion_posfija(expresion)
print("Resultado:", resultado)
