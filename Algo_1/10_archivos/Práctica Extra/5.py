# 5.
# Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
# línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
# nombre;código;precio;stock
# Un posible ejemplo de este archivo es el siguiente:
# lapiceras;34512;50;120
# cuadernos;41611;500;130
# sacapuntas;62812;30;210
# Se pide:
# a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
# Nombre producto: lapiceras
# Código producto: 34512
# Precio por unidad: 50
# Stock: 120
# Nombre producto: cuadernos
# Código producto: 41611
# Precio por unidad: 500
# Stock: 130
# b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue, es
# decir que si se recibe un diccionario del tipo
# {
# “nombre”: “hojas A4”,
# “código”: 35662,
# “precio”: 600,
# “stock”: 45
# }

ruta = "Algo_1\\10_archivos\\Práctica Extra\\archivos\\stock.csv"
# a.
def mostrar_stock(archivo_librería):
    """
    Muestra el stock de productos de una librería desde un archivo de texto.
    Esta función abre un archivo de texto especificado por 'archivo_librería' que contiene información sobre los productos de una librería (nombre, código, precio y stock). Luego, muestra esta información en la consola.
    Parámetros:
    - archivo_librería (str): La ruta del archivo de texto que contiene el stock de la librería.
    """
    with open(archivo_librería, "r") as file_librería:
        stock = file_librería.readlines()
        for línea in stock:
            # Divide la línea en nombre, código, precio y stock utilizando el delimitador ";".
            nombre, código, precio, stock = línea.strip("\n").split(";")
            # Imprime en la consola los detalles de cada producto.
            print(f"Nombre: {nombre}")
            print(f"Código: {código}")
            print(f"Precio: {precio}")
            print(f"Stock: {stock}\n")

# b.
def agregar_producto(archivo_librería, producto: dict):
    """
    Agrega un producto al archivo de una librería.
    Esta función permite agregar un nuevo producto al archivo de una librería representado por 'archivo_libreria' en formato de texto. El producto debe proporcionarse como un diccionario con las claves 'nombre', 'código', 'precio' y 'stock'.
    Parámetros:
    - archivo_libreria (str): La ruta del archivo de la librería en el que se agregará el producto.
    - producto (dict): Un diccionario que contiene la información del producto a agregar, incluyendo 'nombre', 'código', 'precio' y 'stock'.
    """
    with open(archivo_librería, "a") as file_librería:
        nombre = producto["nombre"]
        código = producto["código"]
        precio = producto["precio"]
        stock  = producto["stock"]
        file_librería.write(f"\n{nombre};{código};{precio};{stock}")

producto = {
    "nombre": "HojasA4",
    "código": 35662,
    "precio": 600,
    "stock": 45
}

# Uso de las funciones definidas con anterioridad
agregar_producto(ruta, producto)
mostrar_stock(ruta)