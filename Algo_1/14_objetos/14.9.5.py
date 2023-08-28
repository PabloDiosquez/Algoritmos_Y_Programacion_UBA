# a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
# sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
# b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
# cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
# misma cantidad de elementos debe levantar una excepción.
# c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con
# los elementos multiplicados por ese número.

from helpers import sumar_uno_a_uno, validar_lista_de_números, multiplicar_por_número

class Vector:
    """
    Representa un vector de Rn.
    """

    def __init__(self, elementos: list) -> None:
        """
        """
        self.coordenadas = validar_lista_de_números(elementos)

    def __str__(self) -> str:
        """
        Conversión a cadena de texto.
        """
        return self.coordenadas.__str__()
    
    def dimensión(self):
        """
        Describe la cantidad de elementos del vector.
        """
        return self.vector.__len__()
    
    def __add__(self, otro_vector):
        """
        Recibe otro vector, verifica si tienen la misma cantidad de elementos y describe un nuevo vector con la suma de ambos. Si no tienen la misma cantidad de elementos debe levanta ValueError.
        """
        if not self.dimensión == otro_vector.dimensión:
            raise ValueError("Los vectores deben tener la misma cantidad de elementos")
        return Vector(sumar_uno_a_uno(self.coordenadas, otro_vector.coordenadas))

    def __mul__(self, número):
        """
        Recibe un número y describe un nuevo vector, con los elementos multiplicados por ese número.
        """
        return Vector(multiplicar_por_número(self.coordenadas, número))