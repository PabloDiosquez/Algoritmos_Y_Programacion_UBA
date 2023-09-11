# ¿Cómo implementar una lista?

from _nodo import _Nodo
from iteradores import IteradorListaEnlazada

# ------ Lista 🙊 ------
class ListaEnlazada:
    "Modela una lista enlazada"

    # El método __init__ se encarga de inicializar la lista enlazada.
    def __init__(self):
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len  = 0

    # El método append se utiliza para agregar un nuevo dato al final de la lista
    def append(self, dato):
        nuevo = _Nodo(dato, None)

        if self.prim is None:
            self.prim = nuevo # Caso borde (lista vacía)

        actual = self.prim 
        while actual.prox is not None:
            actual = actual.prox
         # actual es el último _nodo
        actual.prox = nuevo

    def insert(self, i: int, x: any):
        """
        Agrega el elemento 'x' en la posición 'i'.
        Levanta una excepción si la posición dada es inválida.
        """ 
        if i < 0 or i >= self.len: 
            raise IndexError("Índice fuera de rango")
        nuevo = _Nodo(x)
        # Caso particular: insertar al principio
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else: 
            # Buscar el nodo anterior a la posición deseada
            actual   = self.prim 
            for _ in range(1, i):
                actual  = actual.prox
            # Intercalar el nuevo nodo
            nuevo.prox  = actual.prox
            actual.prox = nuevo
        self.len += 1  
        
    def pop(self, i):
        """
        Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento.
        """
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len: 
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato      = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Máquinas de parejas 👫
            # Buscar los nodos en las posiciones (i-1) e (i)
            nodo_anterior = self.prim
            nodo_actual   = nodo_anterior.prox
            for _ in range(1, i):
                nodo_anterior = nodo_actual
                nodo_actual   = nodo_anterior.prox
            # Guardar el dato y descartar el nodo
            dato               = nodo_actual.dato 
            nodo_anterior.prox = nodo_actual.prox   
        self.len -= 1
        return dato 
    
    def remove(self, x):
        """
        Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError.
        """
        if self.prim is None: 
            raise ValueError("Lista vacía")
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
        # Buscar el nodo anterior al que contiene a x (n_ant)
            anterior = self.prim
            actual   = self.prim.dato
            while actual is not None and actual.dato != x:
                anterior = actual 
                actual   = actual.prox 
            if actual is None: 
                raise ValueError("El valor no está en la lista")
            # Descartar el nodo
            anterior.prox = actual.prox  
        self.len -= 1 
             
    def __str__(self) -> str:
        "Representación en cadena de texto de la lista"
        s = "["
        actual = self.prim
        while actual is not None:
            s += f"{str(actual.dato) }"
            actual = actual.prox
        s += "]"
        return ', '.join(s.split(' '))
    
    def __len__(self):
        "Describe la longitud de la lista"
        # Implementación poco eficiente del método.
        # cant_nodos = 0
        # actual = self.prim
        # while actual is not None:
        #     cant_nodos += 1
        #     actual = actual.prox
        # return cant_nodos
        return self.len
    
    def index(self, x: any):
        """
        Describe la posición de la primera aparición del elemento 'x' en la lista enlazada actual.
        Parámetros:
            x (any): El elemento que se busca en la lista. Puede ser de cualquier tipo, ya que la lista enlazada admite almacenar cualquier tipo de dato.
        Retorna:
            int: La posición de la primera aparición de 'x' en la lista enlazada. La posición se cuenta desde cero (0) para el primer elemento de la lista y se incrementa en uno (1) para cada elemento subsiguiente.
        Excepciones:
            ValueError: Se levanta una excepción de tipo ValueError si el elemento 'x' no se encuentra en la lista. Esto indica que el elemento buscado no está presente en la estructura de datos y, por lo tanto, no se puede determinar su posición.
        Ejemplo de uso:
            >>> lista = ListaEnlazada()
            >>> lista.agregar(10)
            >>> lista.agregar(20)
            >>> lista.agregar(30)
            >>> lista.index(20)
            1
        Observaciones:
            - Este método es útil para determinar la posición de un elemento específico en la lista enlazada, lo que puede ser importante en muchos casos de uso.
            - Si hay múltiples apariciones de 'x' en la lista, este método devolverá la posición de la primera aparición.
            - Tener en cuenta que las posiciones se cuentan desde cero (0) en adelante, siguiendo la convención común en la programación.
        """
        if self.prim is None: 
            raise ValueError("Lista vacía")
        actual = self.prim
        índice = 0
        while actual is not None and actual.dato != x:
            actual = actual.prox
            índice += 1
        if actual is None:
            raise ValueError(f'{x} no está en la lista')
        return índice  
    
    def __iter__(self):
        """
        Método especial que debe devolver un iterador para el objeto. El iterador debe ser un objeto que implementa el método __next__.
        """
        return IteradorListaEnlazada(self)