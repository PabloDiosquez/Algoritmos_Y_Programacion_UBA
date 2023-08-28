# a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
# instantes de tiempo (números enteros expresados en segundos), con la condición desde
# < hasta.
# b) Implementar el método duración que devuelve la duración en segundos del intervalo.
# c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo in-
# tervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección
# es nula.
# d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adya-
# centes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
# intervalo resultante de la unión entre ambos.

from helpers import validar_número_entero_positivo

class Intervalo:
    """
    Representa un intervalo entre dos instantes de tiempo.
    """
    
    def __init__(self, desde, hasta):
        """
        Crea un intervalo de tiempo desde 'desde' hasta 'hasta'.
        Precondición:
            - 'desde' y 'hasta' deben ser números enteros.
            -  Debe ser 'desde' < 'hasta'
        """
        self.desde = validar_número_entero_positivo(desde)
        self.hasta = validar_número_entero_positivo(hasta)

    def duración(self):
        """
        Describe la duración en segundos del intevalo.
        """
        return self.hasta - self.desde