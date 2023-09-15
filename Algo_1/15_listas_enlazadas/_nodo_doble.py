class _NodoDoble:
    """
    Clase que modela un nodo con dos referencias: una al siguiente nodo y otra al nodo anterior.
    """
    def __init__(self, dato, prox=None, ant=None):
        """
        Inicializa un nuevo nodo doble.
        Parámetros:
        - dato: El dato almacenado en el nodo.
        - prox: Referencia al siguiente nodo (por defecto, None).
        - ant: Referencia al nodo anterior (por defecto, None).
        """
        self.dato = dato
        self.prox = prox
        self.ant  = ant