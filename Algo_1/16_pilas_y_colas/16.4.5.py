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
            - Si la pila principal está vacía debe estar vacía la pila de máximos. Y por el contrario, si la pila principal no está vacía, no debe estar vacía pila de máximos tampoco.
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
    
# Solución alternativa 🐍 
class PilaConMaximo:
    def __init__(self):
        self.elementos = []  # Pila para almacenar elementos
        self.maximos = []    # Pila para realizar seguimiento de los máximos

    def apilar(self, elemento):
        self.elementos.append(elemento)

        # Si la pila de máximos está vacía o el nuevo elemento es mayor o igual al máximo actual,
        # lo agregamos a la pila de máximos.
        if not self.maximos or elemento >= self.maximos[-1]:
            self.maximos.append(elemento)

    def desapilar(self):
        if not self.elementos:
            return None  # La pila está vacía

        elemento_desapilado = self.elementos.pop()

        # Si el elemento desapilado es igual al máximo actual, lo eliminamos de la pila de máximos.
        if elemento_desapilado == self.maximos[-1]:
            self.maximos.pop()

        return elemento_desapilado

    def obtener_maximo(self):
        if not self.maximos:
            return None  # La pila está vacía

        return self.maximos[-1]

# Ejemplo de uso:
pila = PilaConMaximo()

pila.apilar(3)
pila.apilar(5)
pila.apilar(2)
pila.apilar(7)

print("Máximo actual:", pila.obtener_maximo())  # Debería imprimir 7

pila.desapilar()
pila.desapilar()

print("Máximo actual:", pila.obtener_maximo())  # Debería imprimir 5