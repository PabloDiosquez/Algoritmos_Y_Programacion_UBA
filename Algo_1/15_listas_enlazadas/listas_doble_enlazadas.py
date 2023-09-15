# Una lista doblemente enlazada es una lista en la cual cada nodo tiene una
# referencia al anterior además de al próximo de modo que es posible recorrerla en ambas direcciones. Escribir la clase ListaDobleEnlazada, incluyendo los métodos insert, append, remove y pop.

from _nodo_doble import _NodoDoble

class ListaDobleEnlazada:
    "Modela una lista doblemente enlazada"

    def __init__(self):
        "Inicializa una lista doblemente enlazada" 
        self.prim = None 
        self.ult  = None
        self.len  = 0 

    def append(self, dato: any):
        """
        Agrega un nuevo elemento al final de la lista doblemente enlazada.
        Parámetros:
            - dato (any): El dato que se desea agregar al final de la lista.
        """
        nuevo = _NodoDoble(dato) # Creamos un nuevo nodo con el dato proporcionado.
        # Caso especial: la lista está vacía.
        if self.prim is None:
            self.prim = nuevo 
            self.ult  = nuevo 
        else:
            # Establecemos las conexiones apropiadas para el nuevo nodo.
            nuevo.ant     = self.ult
            self.ult.prox = nuevo   
            self.ult      = nuevo
        self.len += 1 # Incrementamos la longitud de la lista en 1.

    def insert(self, i: int, x: any):
        """
        Inserta en la posición 'i' de una lista doblemente enlazada el elemento 'x'.
        Parámetros:
            - i (int): La posición en la que se insertará el elemento 'x'. El índice de la primera posición es 0.
            - x (any): El elemento que se va a insertar en la lista.
        Observación:
        IndexError: Se lanza si la posición 'i' está fuera de rango, es decir, si 'i' es menor que 0 o mayor o igual que la longitud actual de la lista.
            - Esta función modificará la estructura de la lista doblemente enlazada al insertar el elemento 'x', por lo que la longitud de la lista aumentará en 1 después de la operación.
        """
        if i < 0 or i > self.len:
            raise IndexError("Índice fuera de rango")
        nuevo = _NodoDoble(x)
        # Insertar al principio de la lista
        if i == 0:
            nuevo.prox = self.prim
            if self.prim:
                self.prim.anterior = nuevo 
            self.prim  = nuevo
        # Insertar al final de la lista.
        elif i == self.len:
            nuevo.ant = self.ult
            if self.ult:
                self.ult.prox = nuevo 
            self.ult = nuevo 
        # Insertar en una posición intermedia 
        else:     
            actual   = self.prim 
            for _ in range(i):
                nuevo.prox      = actual
                nuevo.ant       = actual.ant  
                actual.ant.prox = nuevo
                actual.ant      = nuevo     
        self.len += 1    

    def pop(self):
        """
        Elimina el último elemento de una lista doblemente enlazada y lo describe.
        Excepciones:
            - ValueError: Se lanza si la lista doblemente enlazada está vacía al intentar eliminar el último elemento.
        Observación:
            - La función modifica la estructura de la lista al eliminar el último elemento.
            - La longitud de la lista (self.len) se reduce en 1 después de eliminar el elemento.
        """
        if self.prim is None:
            raise ValueError("Lista vacía")
        elemento_eliminado = self.ult.dato
        if self.len == 1:
            self.prim = None
            self.ult  = None
        else:
            self.ult      = self.ult.ant
            self.ult.prox = None 
        self.len -= 1
        return elemento_eliminado  
    
    def remove(self, x: any):
        """
        Elimina el elemento 'x' de una lista doblemente enlazada.
        Parámetros:
            - x (any): El elemento que se desea eliminar de la lista.
        Observaciones:
            - ValueError: Se lanza si la lista doblemente enlazada está vacía o si el elemento 'x' no se encuentra en la lista.
            - La función modifica la estructura de la lista al eliminar el elemento 'x'. Si hay múltiples instancias de 'x' en la lista, solo se eliminará la primera aparición encontrada.
        """
        if self.prim is None:
            raise ValueError("Lista vacía")
        
        actual = self.prim 
        while actual:
            if actual.dato == x:
                if actual.ant:
                    actual.ant.prox = actual.prox
                else:
                    self.prim = actual.prox

                if actual.prox:
                     actual.prox.ant = actual.ant
                else:
                    self.ult = actual.ant  
                actual.prox.ant = actual.ant 
                self.len -= 1
                return   
            actual = actual.prox
        
        raise ValueError(f"El elemento {x} no se encuentra en la lista")