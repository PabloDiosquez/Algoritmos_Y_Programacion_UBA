# 3.
# En un hogar se quieren organizar mejor con las compras, por lo que se quiere guardar en un archivo la
# lista de productos que se necesitan para la próxima vez que la familia vaya al supermercado. Se pide
# hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le
# pregunte al usuario qué necesita comprar hasta que ingrese una X. Por ejemplo
# > ¿Qué agrego a la lista de compras?
# > Papa
# > ¿Qué agrego a la lista de compras?
# > Pollo
# > ¿Qué agrego a la lista de compras?
# > Fideos
# > ¿Qué agrego a la lista de compras?
# > X
# El archivo tendría que estar de la siguiente forma:
# Papa
# Pollo
# Fideos

def crear_compra(ruta):
    """
    Crea una lista de compras en un archivo de texto.
    Esta función permite al usuario ingresar elementos para agregar a una lista de compras y guarda estos elementos en un archivo de texto especificado por 'ruta'.
    Parámetros:
    - ruta (str): La ruta del archivo de texto en el que se guardará la lista de compras.
    Ejemplo de uso:
    >>> crear_compra("compras.txt")
    ¿Qué agrego a la lista de compras?
    Papa
    ¿Qué agrego a la lista de compras?
    Pollo
    ¿Qué agrego a la lista de compras?
    Fideos
    ¿Qué agrego a la lista de compras?
    X
    Lista de compras guardada en 'compras.txt'.
    
    """
    # Abre el archivo en modo escritura ('w')
    with open(ruta, "w") as compra:
        while True:
            # Pide al usuario que ingrese un elemento o 'X' para salir
            producto = input("¿Qué agrego a la lista de compras?\n")
            if producto.upper() == "X": break # Verifica si el usuario quiere salir
            # Escribe el producto en el archivo 
            compra.write(f"{producto}\n")

# Uso de la función definida anteriormente
ruta = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\compra.txt" 
crear_compra(ruta)