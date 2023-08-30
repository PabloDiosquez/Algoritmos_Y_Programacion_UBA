# TDA Pila 📚 LIFO (Last in, First out)

# crear_vacía() ➡ P    O(1)
# apilar(P, x)          O(1)
# desapilar(P)  ➡ x    O(1)
# ver_tope(P)   ➡ x    O(1)
# está_vacía(P) ➡ bool O(1)

class Pila:

    def __init__(self):
        self.apilados = []

    def apilar(self, x):
        self.apilados.append(x)

    def desapilar(self):
        return self.apilados.pop()
    
    def ver_tope(self):
        return self.apilados[len(self.apilados)-1] 

    def está_vacía(self):
        return not len(self.apilados)