# TDA COLA 🐕‍🦺 FIFO (First in, First out)

# crear_vacía()    ➡ C     O(1)
# encolar(C, x)             O(1)
# desencolar(C) ➡ x     O(1)
# ver_frente(C)    ➡ x     O(1)
# está_vacía(C)    ➡ bool  O(1)

class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None 

    def encolar(self, dato):
        pass 
    
    def desencolar(self):
        pass 

    def ver_frente(self):
        pass 

    def está_vacía(self):
        pass 
        

class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato 
        self.prox = prox 