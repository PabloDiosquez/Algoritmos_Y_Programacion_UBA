# Escribir una función que recibe una expresión matemática (en forma de cade-
# na) y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente balanceados, False en caso contrario. Ejemplos:
# validar('(x+y)/2') -> True
# validar('[8*4(x+y)]+{2/5}') -> True
# validar('(x+y]/2') -> False
# validar('1+)2(+3') -> False

from pila_bis import Pila 

def validar(expresion):
    """
    Indica si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente balanceados en la expresión 'expresion'.
    Parámetros:
        - expresion (str): Expresión matemática a validar.
    Retorna:
        - True si la expresión está correctamente balanceada; False en caso contrario.
    """
    # Definir un diccionario para mapear los caracteres de cierre a sus correspondientes caracteres de apertura
    parejas = {"(": ")", "[": "]", "{": "}"}
    # Inicializar una pila vacía
    apilados = Pila()
    # Iterar a través de la expresión
    for símbolo in expresion:
        # Si el carácter es una apertura, agregarlo a la pila
        if símbolo in "([{":
            apilados.apilar(símbolo)
        # Si el carácter es un cierre
        elif símbolo in ")]}":
            # Verificar si la pila está vacía o si el carácter de apertura correspondiente en la cima de la pila no coincide
            if apilados.está_vacía() or parejas[apilados.desapilar()] != símbolo:
                return False
    # Al final, la pila debe estar vacía si todos los paréntesis, corchetes y llaves están balanceados 
    return apilados.está_vacía()
    
print(validar('(x+y)/2')) 
print(validar('[8*4(x+y)]+{2/5}'))
print(validar('(x+y]/2'))
print(validar('1+)2(+3'))