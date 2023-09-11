class _Nodo:
    def __init__(self, dato=None, prox=None):
        """
        Crea un nodo que guarda el dato 'dato' y tiene una referencia al nodo 'prox'.
        :param dato: El dato que se almacenará en el nodo.
        :type dato: any, opcional
        :param prox: El nodo siguiente al nodo actual.
        :type prox: _Nodo, opcional
        """
        self.dato = dato
        self.prox = prox

    def __str__(self) -> str:
        """
        Describe una representación en cadena de texto de un nodo.
        :retorna: Representación en cadena de texto del nodo.
        :rtype: str
        """
        return f"Nodo({self.dato})"