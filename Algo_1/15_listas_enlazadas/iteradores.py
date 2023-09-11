class IteradorListaEnlazada():
    """Almacena el estado de una iteración sobre la ListaEnlazada."""

    def __init__(self, lista):
        "Crea un iterador para la lista dada"
        self.lista = lista
        self.anterior = None 
        self.actual   = lista.prim

    def avanzar(self):
        """
        Avanza la iteración un paso hacia adelante.
        Pre: la iteración no debe haber llegado al final.
        """
        self.actual = self.actual.prox 

    def dato_actual(self):
        """
        Devuelve el elemento en la posición actual de iteración.
        Pre: la iteración no debe haber llegado al final.
        """
        return self.actual.dato

    def está_al_final(self):
        """
        Indica si la iteración llego al final de la lista.
        """
        return self.actual is None   