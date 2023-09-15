# Una lista doblemente enlazada es una lista en la cual cada nodo tiene una
# referencia al anterior además de al próximo de modo que es posible recorrerla en ambas direcciones. Escribir la clase ListaDobleEnlazada, incluyendo los métodos insert, append, remove y pop.

from _nodo_doble import _NodoDoble

class ListaDobleEnlazada:
    "Modela una lista doblemente enlazada"

    def __init__(self):
        "Inicializa una lista doblemente enlazada" 
        self.prim = None 
        self.ult  = None 

    def append(self, dato: any):
        """
        Agrega un nuevo elemento al final de la lista doblemente enlazada.
        Parámetros:
            - dato (any): El dato que se desea agregar al final de la lista.
        """
        nuevo = _NodoDoble(dato)
        if self.prim is None:
            self.prim = nuevo 
            self.ult = nuevo 
        else:
            nuevo.ant     = self.ult
            self.ult.prox = nuevo   
            self.ult      = nuevo 

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
        pass 

    def pop(self):
        """
        Elimina el último elemento de una lista doblemente enlazada.
        Excepciones:
            - ValueError: Se lanza si la lista doblemente enlazada está vacía al intentar eliminar el último elemento.
        """
        pass 
    
    def remove(self, x: any):
        """
        Elimina el elemento 'x' de una lista doblemente enlazada.
        Parámetros:
            - x (any): El elemento que se desea eliminar de la lista.
        Observaciones:
            - ValueError: Se lanza si la lista doblemente enlazada está vacía o si el elemento 'x' no se encuentra en la lista.
            - La función modifica la estructura de la lista al eliminar el elemento 'x'. Si hay múltiples instancias de 'x' en la lista, solo se eliminará la primera aparición encontrada.
        """
        pass 
