# Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
# cuatro o seis. Crear una función que pida al usuario informar el número de jugadores, considerando
# que este puede ingresar:
# ● un valor no válido, por ejemplo, una palabra.
# ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
# ● un valor mayor a 6, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 6
# jugadores.".
# ● un valor impar, como 3 y 5, en cuyo caso, mostrar el mensaje "Debe haber un número par de
# jugadores.".
# ● un valor válido, en cuyo caso, mostrarlo.

def obtener_numero_jugadores():
    """
    Esta función solicita al usuario ingresar el número de jugadores para jugar al truco con un único mazo de cartas españolas.
    Retorna:
        int: El número de jugadores válido (2, 4 o 6).
    """
    while True:
        try:
            numero_jugadores = int(input("Ingrese el número de jugadores (2, 4 o 6): "))
            # Verificar si el número de jugadores es válido
            if numero_jugadores in [2, 4, 6]:
                return numero_jugadores
            elif numero_jugadores < 2:
                print("Debe haber al menos 2 jugadores.")
            elif numero_jugadores > 6:
                print("Se puede jugar con un máximo de 6 jugadores.")
            else:
                print("Debe haber un número par de jugadores.")
        except ValueError:
            print("Por favor, ingrese un valor válido (2, 4 o 6).")

if __name__ == "__main__":
    # Llamamos a la función para obtener el número de jugadores
    numero_de_jugadores = obtener_numero_jugadores()
    # Mostramos el número de jugadores válido
    print("Número de jugadores seleccionado:", numero_de_jugadores)