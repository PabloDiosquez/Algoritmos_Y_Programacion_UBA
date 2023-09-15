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