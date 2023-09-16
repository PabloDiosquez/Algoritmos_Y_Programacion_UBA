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
        return not self.items.__len__() 

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