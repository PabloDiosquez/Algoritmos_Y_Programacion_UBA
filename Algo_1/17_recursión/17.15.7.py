# Escribir una función que calcule recursivamente cuántos elementos hay en
# una pila, suponiendo que la pila sólo tiene los métodos apilar y desapilar, y no altere el
# contenido de la pila.

class Pila:
    def __init__(self):
        "Crea una pila vacía"
        self.apilados = []

    def apilar(self, elemento):
        "Apila el elemento dado en una pila"
        self.apilados.append(elemento)

    def desapilar(self):
        "Desapila el tope de una pila y lo describe"
        self.apilados.pop()

    def está_vacía(self):
        "Indica una la pila está vacía"
        return not len(self.apilados)
    
def contar_elementos_pila(pila: Pila):
    """
    Describe la cantidad de elementos de la pila dada.
    """
    if pila.está_vacía(): return 0 # Caso base 
    else:
        desapilado          = pila.desapilar()
        cantidad_al_momento = contar_elementos_pila(pila) # Se sabe contar la cantidad de elementos de la pila con un elemento menos.
        # Se vuelve a apilar el elemento en la pila para no modificarla.
        pila.apilar(desapilado)

        return 1 + cantidad_al_momento