# Pilas representadas por listas 📚

class Pila:
    """
    Representa una pila con operaciones de apilar, desapilar y
    verificar si está vacía.
       """
    
    def __init__(self):
        """
        Crea una pila vacía.
        """
        self.items = []

    def está_vacía(self):
        """
        Indica si la pila está vacía.
        """
        return len(self.items) == 0

    def apilar(self, x: any):
        """
        Apila el elemento 'x'.
        """
        self.items.append(x)
    
    def desapilar(self):
        """
        Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción.
        """
        if self.está_vacía():
            raise ValueError("La pila está vacía")
        return self.items.pop()

    def ver_tope(self):
        """
        Describe el tope de la pila dada.
        Si la pila está vacía levanta una excepción.
        """ 
        if self.está_vacía:
            raise ValueError("Pila vacía")
        return self.items[-1]