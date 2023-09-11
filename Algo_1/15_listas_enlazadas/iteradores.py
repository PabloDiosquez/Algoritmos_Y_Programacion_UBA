from listas_enlazadas import _Nodo

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

    def insertar(self, x: any):
        """
        Insertar un elemento en el lugar de la iteración actual.
        Una vez insertado, el nuevo elemento será el actual de la iteración,
        y el elemento que antes era el actual será el siguiente.
        """ 
        nuevo = _Nodo(x)
        if self.anterior:
            nuevo.prox         = self.anterior.prox 
            self.anterior.prox = nuevo
        else: 
            nuevo.prox      = self.lista.prim
            self.lista.prim = nuevo 
        self.actual = nuevo  

    def eliminar(self, x: any):
        """
        Elimina el nodo que contiene el dato 'x' de la lista enlazada.
        Si el nodo con el dato 'x' se encuentra en una posición intermedia de la lista,
        este método ajustará las referencias de los nodos adyacentes para eliminarlo.
        Si el nodo con el dato 'x' es el primero en la lista, se actualizará el puntero
        inicial de la lista.
        """
        if self.anterior:
            self.anterior.prox = self.actual.prox
            self.actual        = self.anterior.prox
        else:
            self.lista.prim = self.actual.prox 
            self.actual = self.lista.prim  
        return self.dato_actual()