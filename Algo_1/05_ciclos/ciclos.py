# Ciclos definidos 🌀

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

# Ciclo indefinido 🌀 

# while <condición>:
#     <instrucciones>

def caja_registradora_version2():
    suma = 0

    while True:
        precio = float(input("Precio del producto -- 0 para cortar --: "))
        if precio == 0: break 
        suma += precio 
        print("La suma es:", suma)
        
    print("\nLa suma total es:", suma)

caja_registradora_version2()