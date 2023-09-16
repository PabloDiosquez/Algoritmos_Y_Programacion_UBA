# La famosa calculadora portátil HP-35 (de 1972) popularizó la notación polaca inversa (o
# notación prefijo) para hacer cálculos sin necesidad de usar paréntesis. Esa notación, inventada
# por el lógico polaco Jan Lukasiewicz en 1920, se basa en el principio de que un operador siempre
# se escribe a continuación de sus operandos. La operación (5−3)+8 se escribirá como 5 3 - 8 +,
# que se interpretará como: “restar 3 de 5, y al resultado sumarle 8”.
# Es posible implementar esta notación de manera sencilla usando una pila de la siguiente
# manera, a partir de una cadena de entrada de valores separados por blancos:
# • Mientras se lean números, se apilan.
# • En el momento en el que se detecta una operación binaria +, -, * o / se desapilan los dos úl-
# timos números apilados, se ejecuta la operación indicada, y el resultado de esa operación
# se apila.
# • Si la expresión está bien formada, tiene que quedar al final un único número en la pila (el
# resultado).
# • Los posibles errores son:
# – Queda más de un número al final (por ejemplo si la cadena de entrada fue "5 3"),
# – Ingresa algún caracter que no se puede interpretar ni como número ni como una de
# las cinco operaciones válidas (por ejemplo si la cadena de entrada fue "5 3 &")
# – No hay suficientes operandos para realizar la operación (por ejemplo si la cadena
# de entrada fue "5 3 - +").
# La siguiente es la estrategia de resolución:
# Dada una cadena con la expresión a evaluar, podemos separar sus componentes utilizando
# el método split. Recorreremos luego la lista de componentes realizando las acciones indicadas
# en el párrafo anterior, utilizando una pila auxiliar para operar. Si la expresión está bien formada
# devolveremos el resultado, de lo contrario levantaremos una excepción.

from pila_bis import Pila

def calculadora_polaca(elementos):
    """
    Dada una lista de elementos que representan las componentes de
    una expresión en notacion polaca inversa, evalúa dicha expresión.
    Si la expresion está mal formada, levanta ValueError.
    """
    p = Pila()
    for elemento in elementos:
        print("DEBUG: ", elemento)
        # Intenta convertirlo a número
        try:
            número = float(elemento)
            p.apilar(número)
            print("DEBUG: apila", número)
        # Si no se puede convertir a número, debería ser un operador.
        except ValueError:
            # Si no es un operador válido, levanta ValueError.
            if elemento not in ('+', '-', '*', '/'):
                raise ValueError("Operando inválido")
            # Si es un operador válido intenta desapilar y operar.
            try:
                operando1 = p.desapilar()
                print("DEBUG: desapila ", operando1)
                operando2 = p.desapilar()
                print("DEBUG: desapila ", operando2)
            # Si hubo problemas al desapilar.
            except IndexError:
                raise ValueError("Faltan operandos")

            if elemento == '+':
                resultado = operando2 + operando1
            elif elemento == '-':
                resultado = operando2 - operando1
            elif elemento == '*':
                resultado = operando2 * operando1
            elif elemento == '/':
                resultado = operando2 / operando1
            print("DEBUG: apila ", resultado)
            p.apilar(resultado)
        
    # Al final el resultado debe ser lo único en la pila.
    resultado = p.desapilar()
    if not p.está_vacía():
        raise ValueError("Sobran operandos")
    return resultado
         
def main():
    expresión = input("Ingrese la expresión a evaluar: ")
    elementos = expresión.split(" ")
    print(calculadora_polaca(elementos))

main()         