# ¿Cómo implementar una lista?

# ------ Nodo 🙊 ------
class ListaEnlazada:
    # El método __init__ se encarga de inicializar la lista enlazada. El atributo self.prim se utiliza para almacenar el primer nodo de la lista. Al inicio, la lista está vacía, por lo que se establece self.prim como None.
    def __init__(self):
        self.prim = None

    # El método append se utiliza para agregar un nuevo dato al final de la lista
    def append(self, dato):
        nuevo = Nodo(dato, None)

        if self.prim is None: self.prim = nuevo # Caso borde (lista vacía)

        actual = self.prim 
        while actual.próx is not None:
            actual = actual.próx
         # actual es el último nodo
        actual.próx = nuevo 
    
    def __str__(self) -> str:
        s = str()
        
        actual = self.prim
        while actual.próx is not None:
            s += f"{str(actual) }"
        s += f"{str(actual)}"
        return s

         
# ------ Nodo 🙈 ------
class Nodo:
    
    def __init__(self, dato, próx):
        self.dato = dato 
        self.próx = próx 

    def __str__(self) -> str:
        return f"Nodo({self.dato})"


# ------ Main 🙉 ------
def main():
    # n1 = Nodo('a', None)
    # print(n1)
    # n2 = Nodo('b', None)
    # n1.próx = n2 
    # print(n1.próx)
    # print(n2)

    L = ListaEnlazada()
    L.append('a')
    L.append('b')
    L.append('c')

    print(str(L))


main()