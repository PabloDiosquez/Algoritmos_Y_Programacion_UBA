# TDA Pila 📚 LIFO (Last in, First out)

# crear_vacía() ➡ P    O(1)
# apilar(P, x)          O(1)
# desapilar(P)  ➡ x    O(1)
# ver_tope(P)   ➡ x    O(1)
# está_vacía(P) ➡ bool O(1)

# Implementación con _nodos 

# ------ Pila ------
class Pila:

    def __init__(self):
        self.tope = None 

    def apilar(self, dato):
        # nuevo_tope = _Nodo(dato, self.tope)
        # self.tope  = nuevo_tope
        self.tope = _Nodo(dato, self.tope)

    def desapilar(self):
        """
        Elimina el tope de la pila y lo describe.
        Pre:
            - La pila no debe estar vacía.
        """
        if self.tope is None:
            raise ValueError("Pila vacía")
        viejo_tope = self.tope.dato
        self.tope  = self.tope.prox
        return viejo_tope  
    
    def ver_tope(self):
        """
        Describe el tope de la lista.
        Pre:
            - La pila no debe estar vacía.
        """
        if self.tope is None:
            raise ValueError("Pila vacía")
        return self.tope.dato  

    def está_vacía(self):
        """
        Indica si la pila está vacía.
        """
        return self.tope is None  
    
# ------ Nodo ------
class _Nodo:

    def __init__(self, dato, prox):
        self.dato = dato 
        self.prox = prox

def main():
    p = Pila()
    p.apilar('x')
    p.apilar('z')
    p.apilar('a')
    
    print(p.ver_tope())
    p.desapilar()
    print(p.ver_tope())
    p.desapilar()
    print(p.ver_tope())
    p.desapilar()
    print(p.está_vacía())
    
main()