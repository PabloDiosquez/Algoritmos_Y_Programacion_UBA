# 8.
# El kiosko de la facultad quiere automatizar un letrero que tome datos de un programa y le cobre al
# estudiante.
# Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada
# producto.
# Ejemplo:
# opciones = {
# 1: "hamburguesas",
# 2: "milanesas",
# 3: "gaseosa",
# 4: "alfajor",
# 5: "papas fritas",
# 6: "agua"
# }

# valores = {
# 1:1000,
# 2:1500,
# 3:500,
# 4:300,
# 5:600,
# 6:350
# }

# Se quiere hacer un programa que muestre la información de la siguiente forma en la pantalla:
# 1: hamburguesas -> 1000
# 2: milanesas -> 1500
# 3: gaseosa -> 500
# 4: alfajor -> 300
# 5: papas fritas -> 600
# 6: agua -> 350
# Y le pida al usuario una opción y una cantidad. Luego, debe imprimir el total a pagar.
# Se debe considerar que el usuario podría ingresar una opción que no está en el diccionario, o ingresar
# una opción que no sea un número. El usuario debe en esos casos imprimir un mensaje de error que sea
# descriptivo y volver a pedirle al usuario que ingrese una opción.

def mostrar_opciones_y_valores(opciones: dict, valores: dict):
    """
    Esta función muestra en la pantalla el menú de opciones con códigos, productos y precios.
    Parámetros:
        - opciones (dict): Un diccionario que contiene los códigos y productos.
        - valores (dict): Un diccionario que contiene los códigos y precios de los productos.
    """
    print("Menú de opciones 🍔")
    for código, producto in opciones.items():
         precio = valores[código]
         print(f"{producto} ➡ ${precio}")

def total_a_pagar(opciones, valores):
    """
    Esta función solicita al usuario una opción y una cantidad, y calcula el total a pagar.
    Parámetros:
        - opciones (dict): Un diccionario que contiene los códigos y productos.
        - valores (dict): Un diccionario que contiene los códigos y precios de los productos.
    Retorna:
        float: El total a pagar.
    """
    while True:
        try:
            opcion = int(input("Ingrese el código del producto: "))
            if opcion in opciones:
                cantidad = int(input("Ingrese la cantidad: "))
                precio_unitario = valores[opcion]
                total = precio_unitario * cantidad
                return total
            else:
                print("Opción no válida. Por favor, ingrese un código de producto válido.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
        # Diccionarios con opciones y valores
        opciones = {
        1: "hamburguesas",
        2: "milanesas",
        3: "gaseosa",
        4: "alfajor",
        5: "papas fritas",
        6: "agua"
        }

        valores = {
        1:1000,
        2:1500,
        3:500,
        4:300,
        5:600,
        6:350
        }

        # Calcular el total a pagar
        total_pagar = total_a_pagar(opciones, valores)
        # # Mostrar el total a pagar al usuario
        print(f"Total a pagar: ${total_pagar}")