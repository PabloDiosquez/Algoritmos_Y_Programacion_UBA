from helpers import get_int

def ciclo_definido(inicio, fin):
    """Imprime por consola todos los números entre *inicio* y **fin** inclusive.
    """
    print(f"Números entre {inicio} y {fin} inclusive:")
    for i in range(inicio, fin+1):
        print(i, end=" ")

print("- Ejercicio 2.6.1.a -")
ciclo_definido(10, 20)

def saludar_amigos(numero_amigos):
    for _ in range(numero_amigos):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}!")

#print("- Ejercicio 2.6.1.b -")
#saludar_amigos(5)

def saludar_amigos():
    numero_amigos = get_int("¿A cuántos amigos desea saludar?")
    for _ in range(numero_amigos):
        nombre = input("Nombre: ")
        print(f"Hola {nombre}!")

print("- Ejercicio 2.6.1.e -")
saludar_amigos()