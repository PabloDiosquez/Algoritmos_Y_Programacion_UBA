# TDA COLA 🐕‍🦺 FIFO (First in, First out)

# crear_vacía()    ➡ C     O(1)
# encolar(C, x)             O(1)
# desencolar(C) ➡ x        O(1)
# ver_frente(C)    ➡ x     O(1)
# está_vacía(C)    ➡ bool  O(1)

# Implementación con nodos 

# ----- Clase Cola ------
class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None 

    def encolar(self, dato):
        nuevo            = _Nodo(dato, None)
        if self.ultimo is None:
            # cola vacía
            self.frente = nuevo
        else:
            self.ultimo.prox = nuevo
        self.ultimo      = nuevo
    
    def desencolar(self):
        """
        Desencola el primer elemento y lo describe.
        Invariante de la clase:
            - 'frente' y 'ultimo' o bien ambos son None o bien los dos son un nodo
        Precondición:
            - La cola no puede ser vacía.
        """ 
        viejo_frente = self.frente.dato
        self.frente  = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return viejo_frente  

    def ver_frente(self):
        """
        Indica si la cola está vacía.
        Invariante de la clase:
            - 'frente' y 'ultimo' o bien ambos son None o bien los dos son un nodo
        """
        return self.frente.dato 

    def está_vacía(self):
        return self.frente is None  
        
# ----- Clase Nodo privada ------
class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato 
        self.prox = prox 

def main():
    c = Cola()
    c.encolar('🌳')
    c.encolar('🚀')
    c.encolar('🐀')
    print(c.ver_frente())
    c.desencolar()
    c.desencolar()
    c.desencolar()
    print(c.está_vacía())

main()