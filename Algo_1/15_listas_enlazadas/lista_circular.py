# 15.9.7. Una lista circular es una lista cuyo último nodo está ligado al primero, de
# modo que es posible recorrerla infinitamente. Escribir la clase ListaCircular, incluyendo los métodos insert, append, remove y pop.

from _nodo import _Nodo

class ListaCircular:
    "Modela una lista circular en la que el último nodo está ligado al primero, de modo que es posible recorrerla infinitamente."

    def __init__(self):
        """
        Inicializa una nueva instancia de una lista circular vacía.
        """
        self.prim      = None
        self.ult       = None
        self.len       = 0  

    def append(self, x):
        """
        Inserta un nuevo nodo con el valor dado al final de la lista circular.
        Parámetros:
            - x (any): El valor que se va a insertar en el nuevo nodo.
        """
        nuevo = _Nodo(x)
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y el último.
        if self.prim is None: 
            self.prim = nuevo
            self.ult  = nuevo
            self.ult.prox = self.prim
        else:
            # Si la lista no está vacía, el nuevo nodo se convierte en el último y se enlaza con la cabeza.
            self.ult.prox = nuevo 
            self.ult      = nuevo   
            self.ult.prox = self.prim # Establecer enlace circular
        self.len += 1

    def pop(self):
        """
        Elimina y describe el último elemento de una lista. Si la lista está vacía lanza ValueError.
        """
        if self.prim is None:
            raise ValueError("Lista circular vacía")
        # Valor a eliminar 
        eliminado = self.ult.dato
        # Si solo hay un nodo en la lista, la lista queda vacía.
        if self.prim == self.ult:
            self.prim = None
            self.ult  = None
        # Buscar el nodo anterior al último nodo.
        else:
            actual = self.prim 
            while actual.prox is not self.ult:
                actual = actual.prox
            # Actualizar el último nodo y el enlace circular.
            actual.prox = self.prim
            self.ult    = actual
        self.len -= 1
        return eliminado