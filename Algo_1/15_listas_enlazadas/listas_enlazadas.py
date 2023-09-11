# ¿Cómo implementar una lista?

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

    def __pop__(self, i):
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
            for index in range(1, i):
                nodo_anterior = nodo_actual
                nodo_actual   = nodo_anterior.prox
            # Guardar el dato y descartar el nodo
            dato               = nodo_actual.dato 
            nodo_anterior.prox = nodo_actual.prox   

        self.len -= 1
        return dato 
             
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
    
    def ver_lista(self):
        """
        Recorre todos los nodos de la lista a través de sus enlaces, mostrando sus contenidos. 
        """
        actual = self.prim
        while actual is not None:
            print(actual)
            actual = actual.prox
    
# ------ _Nodo 🙈 ------
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

# ------ Main 🙉 ------
def __init__():
    # n1 = _Nodo('a', None)
    # print(n1)
    # n2 = _Nodo('b', None)
    # n1.prox = n2 
    # print(n1.prox)
    # print(n2)

    L = ListaEnlazada()
    L.append('a')
    L.append('b')
    L.append('c')

    L.ver_lista()

__init__()