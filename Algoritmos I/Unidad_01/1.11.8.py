from helpers import get_int, ejercicio

def las_cuatro_operaciones_basicas():
    """Dados dos números enteros, imprime por consola la suma, la resta,
    la multiplicación y la división entre ellos.
    """
    num1 = get_int("Número 1:")
    num2 = get_int("Número 2:")
    print(f"Suma: {num1+num2}")
    print(f"Resta: {num1-num2}")
    print(f"Multiplicación: {num1*num2}")
    if num2 != 0:
        print(f"División: {round(num1/num2,2)}")

ejercicio("1.11.8.a - Todas las operaciones", las_cuatro_operaciones_basicas())

def tabla_del():
    """Imprime por consola la tabla de multiplicar del número dado."""
    numero = get_int("Número:")
    for i in range(11):
        print(f"{numero} x {i} = {numero*i}")

ejercicio("1.11.8.b - Tabla de multiplicar", tabla_del())