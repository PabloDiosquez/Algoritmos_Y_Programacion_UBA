# Funciones ☂
def hola_grace():
    return "Hola Grace!"

def hola_alan():
    return "Hola Alan!"

def hola_(nombre: str) -> str:
    return f"Hola {nombre}!"

def cuad(numero):
    """Describe el cuadrado del número dado.
    """
    return numero*numero

def suma_5_cuadrados():
    """Describe la suma de los primeros 5 números naturales, 
    elevados al cuadrado.
    """
    total = 0
    for i in range(1,6):
        total += cuad(i)
    return total

print(suma_5_cuadrados())