# Colas implementadas sobre listas ⭐

class Cola:
    """
    Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado.
    """

    def __init__(self):
        """
        Crea una cola vacía.
        """
        self.items = []

    def está_vacía(self):
        """
        Indica si la cola está vacía.
        """ 
        return len(self.items) == 0

    def encolar(self, x: any):
        """
        Encola el elemento 'x'
        """
        self.items.append(x)

    def desencolar(self):
        """
        Desencola el elemento 'x'.
        Si la cola está vacía lanza ValueError.
        """
        if self.está_vacía():
            raise ValueError("Cola vacía")
        return self.items.pop(0)