from helpers import ejercicio

def repeticiones(rep):
    """Imprime la palabra leída por consola tantas veces como el número de repeticiones dado.
    """
    palabra = input("Palabra:")
    for _ in range(rep):
        print(palabra, end=" ")

ejercicio("1.11.9 - Repeticiones:", repeticiones(1000))