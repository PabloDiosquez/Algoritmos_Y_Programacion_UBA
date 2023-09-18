# 13.
# a.
def ingresar_fichas(cantidad_fichas: int):
    """
    Recibe un número que representa el precio de la máquina e imprime por pantalla "Ingresá 'x' fichas para comenzar" hasta que se hayan ingresado esa cantidad de letras F (representan un ficha) y luego ¡A jugar! cuando se hayan ingresado todas las fichas necesarias.
    """
    cantidad_fichas_al_momento = 0
    while cantidad_fichas_al_momento < cantidad_fichas:
        ficha = input(f"Ingresá {cantidad_fichas} fichas para comenzar: ")
        if ficha == "F":
            cantidad_fichas_al_momento += 1
    print("¡A jugar!")

# b.
def ingresar_fichas(cantidad_fichas: int):
    """
    Recibe un número que representa el precio de la máquina e imprime por pantalla un mensaje que muestra cuántas fichas faltan (letras F) para poder jugar. En caso de recibir un valor que no corresponde a una ficha real, imprime un error.
    """
    cantidad_fichas_al_momento = 0
    while cantidad_fichas_al_momento < cantidad_fichas:
        ficha = input(f"Ingresa {cantidad_fichas - cantidad_fichas_al_momento} fichas para jugar: ")
        if ficha == "F":
            cantidad_fichas_al_momento += 1
        else: 
            print("Por favor ingrese solo fichas reales (F)") 
    print("¡A jugar!")

ingresar_fichas(3)