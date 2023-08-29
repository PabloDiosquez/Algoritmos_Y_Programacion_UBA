# ¿Cómo implementar una lista?

# ------ Lista 🙊 ------
class ListaEnlazada:
    # El método __init__ se encarga de inicializar la lista enlazada. El atributo self.prim se utiliza para almacenar el primer _nodo de la lista. Al inicio, la lista está vacía, por lo que se establece self.prim como None.
    def __init__(self):
        self.prim = None

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
    
    def __str__(self) -> str:
        s = "["
        
        actual = self.prim
        while actual is not None:
            s += f"{str(actual.dato) }"
            actual = actual.prox
        s += "]"
        return ', '.join(s.split(' '))
    
    def __len__(self):
        cant_nodos = 0
        actual = self.prim
        while actual is not None:
            cant_nodos += 1
            actual = actual.prox
        return cant_nodos

# ------ _Nodo 🙈 ------
class _Nodo:
    
    def __init__(self, dato, prox):
        self.dato = dato 
        self.prox = prox 

    def __str__(self) -> str:
        return f"Nodo({self.dato})"


# ------ Main 🙉 ------
def main():
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

    print(str(L))


main()