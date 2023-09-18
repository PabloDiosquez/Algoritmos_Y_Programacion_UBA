# Crear una clase PilaConMaximo que soporte las operaciones de Pila
# (apilar(elemento) y desapilar()), y además incluya el método obtener_maximo() en tiem-
# po constante. Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los
# máximos.

from pila_bis import Pila

class PilaConMáximo():
    """
    Modela una estructura que combina las operaciones de Pila (apilar(elemento) y desapilar())
    y proporciona el método obtener_máximo() en tiempo constante.
    Invariante:
            - Si la pila principal está vacía debe estar vacía la pila de máximos.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase PilaConMáximo.
        Esta estructura de datos consta de dos pilas: una para almacenar los elementos y otra para
        mantener un registro de los máximos elementos en la pila principal.
        """
        self.pila    = Pila()   # Pila principal para almacenar elementos.
        self.máximos = Pila()   # Pila auxiliar para mantener el registro de máximos.

    def apilar(self, x: any):
        """
        Apila el elemento 'x' en una pila con máximo.
        Parámetros:
            - x (any): El elemento a apilar. 
        """
        if self.pila.está_vacía():
            self.pila.apilar(x)
            self.máximos.apilar(x) 
        else:
            # Apilar el elemento en la pila principal.
            self.pila.apilar(x)
            # Actualizar el máximo en la pila de máximos.
            if x > self.máximos.ver_tope():
                self.máximos.apilar(x)

    def desapilar(self):
        """
        Elimina y luego describe el elemento en el tope de la pila.
        Pre:
            - La pila dada no debe ser vacía. En caso de serlo, lanza ValueError.
        Retorna:
            - El elemento en el tope de la pila.
        """
        if self.pila.está_vacía():
            raise ValueError("Pila vacía")
        
        desapilado = self.pila.desapilar()
        if desapilado == self.máximos.ver_tope():
            self.máximos.desapilar()
        return desapilado 

    def obtener_máximo(self):
        """
        Describe el elemento más grande de una pila.
        Pre:
            - La pila no debe ser vacía. En caso de serlo, lanza ValueError.
        Retorna:
            - El elemento más grande actualmente en la pila.
        """
        if self.pila.está_vacía():
            raise ValueError("Pila vacía")
        return self.máximos.ver_tope()
    
# Usa dos pilas: Como se menciona en la pregunta, la clave para resolver este problema es utilizar dos pilas. Una pila contendrá los elementos que se van apilando y desapilando como de costumbre, mientras que la otra pila contendrá los máximos en cada momento.

# Actualizar la pila de máximos: Cada vez que apiles un elemento en la pila principal, verifica si es mayor que el elemento actual en la pila de máximos. Si es así, apila este nuevo elemento en la pila de máximos. Si no, simplemente repite el elemento actual en la pila de máximos. Esto asegurará que la pila de máximos siempre tenga el máximo valor en la parte superior.

# Eliminar elementos de la pila de máximos: Cuando desapiles un elemento de la pila principal, también verifica si este elemento es igual al elemento actual en la pila de máximos. Si son iguales, también desapila el elemento de la pila de máximos, ya que ese elemento ya no es el máximo en la pila principal.

# Obtener el máximo en tiempo constante: Para obtener el máximo en tiempo constante, simplemente mira el elemento en la parte superior de la pila de máximos en cualquier momento. Ese elemento será el máximo valor en la pila principal en ese momento