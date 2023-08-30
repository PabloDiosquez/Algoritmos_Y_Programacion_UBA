# TDA Pila 📚 LIFO (Last in, First out)

# crear_vacía() ➡ P    O(1)
# apilar(P, x)          O(1)
# desapilar(P)  ➡ x    O(1)
# ver_tope(P)   ➡ x    O(1)
# está_vacía(P) ➡ bool O(1)



# Implementación con nodos 

class Pila:

    def __init__(self):
        self.tope = None 

    def apilar(self, dato):
        # nuevo_tope = Nodo(dato, self.tope)
        # self.tope  = nuevo_tope
        self.tope = Nodo(dato, self.tope)

    def desapilar(self):
        pass 
    
    def ver_tope(self):
        pass  

    def está_vacía(self):
        pass 
    

class Nodo:

    def __init__(self, dato, prox):
        self.dato = dato 
        self.prox = prox