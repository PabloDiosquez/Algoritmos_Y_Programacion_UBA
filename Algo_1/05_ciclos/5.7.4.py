# Utilizando la función randrange del módulo random, escribir un programa que
# obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
# si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
# correcto.

def adivina_el_número(inicio: int, fin: int):
    """
    Juego para adivinar un número secreto dentro de un intervalo dado.
    Parámetros:
        - inicio (int): Borde izquierdo del intervalo al cual pertenece el número secreto.
        - fin (int): Borde derecho del intervalo al cual pertenece el número secreto.
    Precondición:
        - 'inicio' debe ser menor que 'fin'.
    Esta función implementa un juego donde el objetivo es adivinar un número secreto que se encuentra dentro
    del intervalo especificado (inclusive). El jugador debe ingresar números y se le proporcionarán pistas sobre
    si el número secreto es mayor o menor que el número ingresado. El juego continúa hasta que el jugador
    adivina el número secreto. Se muestra el número de intentos realizados.
    Ejemplo de uso:
        >>> adivina_el_número(1, 100)
        Ingrese número: 50
        El número secreto es mayor que el que ingresaste. ¡Intenta de nuevo!
        Ingrese número: 75
        El número secreto es menor que el que ingresaste. ¡Intenta de nuevo!
        Ingrese número: 63
        El número secreto es mayor que el que ingresaste. ¡Intenta de nuevo!
        Ingrese número: 69
        El número secreto es menor que el que ingresaste. ¡Intenta de nuevo!
        Ingrese número: 66
        ¡Adivinaste! Luego de 5 intentos lograste dar con el número secreto ➡ 66
    """
    from random import randrange
    # Genera un número secreto dentro del intervalo [inicio, fin]
    nro_secreto = randrange(inicio, fin+1)
    # Inicializa el contador de intentos
    intentos = 1
    # Bucle principal del juego
    while True:
        user_guess = int(input('Ingrese número: '))
        if user_guess == nro_secreto:
            print(f"¡Adivinaste! Luego de {intentos} intentos lograste dar con el número secreto ➡ {nro_secreto}")
            break
        elif user_guess > nro_secreto:
            print("El número secreto es menor que el que ingresaste. ¡Intenta de nuevo!")
        else:
            print("El número secreto es mayor que el que ingresaste. ¡Intenta de nuevo!")
        intentos += 1

adivina_el_número(1, 10)