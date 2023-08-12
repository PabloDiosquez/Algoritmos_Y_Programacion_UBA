# CICLO DEFINIDO 🌀

# ∀ x ∈ a <iterable>: 
#   procesar x 

# Instrucción ➡ Ciclo definido 
# for <nombre> in <expresión>:
#     <instrucciones>

def caja_registradora_version1():
    suma = 0

    cantidad = int(input("¿Cuántos productos tenés? "))

    for _ in range(cantidad):
        precio = float(input("Precio del producto: "))
        suma += precio   # suma = suma + precio
        print("La suma es:", suma) 

# caja_registradora_version1()

# CICLO INDEFINIDO 🌀 

# while <condición>:
#     <instrucciones>
# Patrón con centinela 🎯
CENTINELA = ""
def caja_registradora_version2():
    suma = 0
    centinela = input("¿Precio del producto?: ")
    while centinela != CENTINELA:
        precio = float(centinela)
        suma += precio 
        print("La suma es:", suma)
        centinela = input("¿Precio del producto?: ")

    print("\nLa suma total es:", suma)

# caja_registradora_version2()

def caja_registradora_version3():
    suma = 0
    res = input("¿Precio del producto?: ")
    while res: # mientras res no sea una cadena vacía...
        suma += float(res)
        print("La suma es:", suma)
        res = input("¿Precio del producto?: ")

    print("\nLa suma total es:", suma)
    
# caja_registradora_version3()

def caja_registradora():
    suma = 0
    while True:
        precio = float(input("¿Precio del producto?: "))
        if precio == 0: break
        suma += precio
        print("La suma hasta ahora es:", suma)
    print("La suma total es:", suma)

caja_registradora()