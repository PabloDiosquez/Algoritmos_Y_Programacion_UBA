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

    def append(self, x: any):
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
    
    def insert(self, i: int, x: any):
        """
        Inserta el elemento 'x' en la posición 'i' de una lista. Si el índice está fuera de rango (menor que 0 o mayor o igual que la longitud de la lista) lanza IndexError.
        Parámetros:
            - i: La posición en la que se va a insertar el nuevo nodo (0 <= i < longitud de la lista).
            - x: El valor que se va a insertar en el nuevo nodo.
        """
        # Posición inválida
        if i < 0 or i >= self.len:
            raise IndexError('Índice fuera de rango')
        nuevo  =_Nodo(x)
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza y el último.
        if self.prim is None:
            self.prim     = nuevo
            self.ult      = nuevo
            self.ult.prox = self.prim
        # Si la posición es 0, el nuevo nodo se inserta antes de la cabeza.
        if i == 0:
            nuevo.prox    = self.prim
            self.prim     = nuevo 
            self.ult.prox = self.prim
        else:
            actual = self.prim
            for _ in range(1, i):
                actual = actual.prox 
            nuevo.prox = actual.prox
            actual.prox = nuevo

        self.len += 1  

    def remove(self, x: any):
        """
        Elimina la primera aparición del elemento 'x' en una lista circular.
        Parámetros:
            - x (any): El elemento cuya primera aparición se va a eliminar de la lista.
        Retorna:
            - bool: True si la eliminación es correcta; False en caso contrario o si la lista está vacía.
        """
        if self.prim is None: 
            raise ValueError("Lista vacía")
        if self.prim.dato == x:
            if self.prim.prox is self.ult: # La lista tiene un solo elemento
                self.prim = None
                self.ult  = None
            else:
                self.prim     = self.prim.prox
                self.ult.prox = self.prim  
            return True 
        # Recorre la lista hasta encontrar el elemento o volver al inicio
        actual   = self.prim
        anterior = self.ult 
        while actual.prox is not self.prim:
            if actual.dato == x:
                anterior.prox = actual.prox
                return True
            aux      =  actual
            actual   = actual.prox
            anterior = aux
        return False           