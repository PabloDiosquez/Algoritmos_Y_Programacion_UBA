# Ejercicio 6.9.9. Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
# el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
# número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
# pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe
# devolver.
# Ejemplo:
# >>> z = pedir_entero("¿Cuál es tu número favorito?", -50, 50)
# ¿Cuál es tu número favorito? [-50..50]:
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: hola
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: -60
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: 51
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: -16
# >>> z
# -16

def pedir_entero(mensaje: str, mín: int, máx: int):
    while True:
        número = input(mensaje)
        if número[1:].isdecimal() and mín <= int(número) <= máx: break 
        print(f"Por favor ingresa un número entre {mín} y {máx}.")
    return número     

def pedir_entero(mensaje, min, max):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < min or valor > max:
                print(f"Por favor, ingresa un número entre {min} y {max}.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.") 

# print(pedir_entero("¿Cuál es tu número favorito?", -50, 50))