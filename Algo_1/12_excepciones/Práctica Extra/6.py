# 6.
# Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
# tres o cuatro. Crear una función que pida al usuario informar el número de jugadores, considerando
# que este puede ingresar:
# ● un valor no válido, por ejemplo, una palabra.
# ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
# ● un valor mayor a 4, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 4
# jugadores."
# ● un valor válido, en cuyo caso, mostrarlo.

def número_jugadores_chinchón():
    """
    Pide al usuario que ingrese el número de jugadores para jugar al chinchón.
    Retorna:
        int: El número de jugadores ingresado.
    """
    while True:
        try:
            número_jugadores = int(input("Ingresa número de jugadores:\n"))
            if número_jugadores < 2:
                print("Debe haber al menos 2 jugadores.")
                continue
            elif número_jugadores > 4:
                print("Se puede jugar con un máximo de 4 jugadores.")
                continue
            return número_jugadores
        except ValueError: 
            print("Valor NO válido. Asegúrese de ingresar un número entero.")

# Ejemplo de uso:
if __name__ == "__main__":
    num_jugadores = número_jugadores_chinchón()
    print("Número de jugadores:", num_jugadores)