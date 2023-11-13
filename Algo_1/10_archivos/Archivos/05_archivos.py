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
# …
# b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue, es
# decir que si se recibe un diccionario del tipo
# {
# “nombre”: “hojas A4”,
# “código”: 35662,
# “precio”: 600,
# “stock”: 45
# }

def obtener_productos():
    """
    Lee el archivo 'stock.csv' y devuelve una lista de listas con la información de los productos.
    Cada lista contiene los datos de un producto: nombre, código, precio y stock.
    """
    with open('archivos/stock.csv', 'r', encoding='UTF-8') as stock:
        return [producto.strip().split(';') for producto in stock.readlines()]

def imprimir_productos():
    """
    Imprime en consola la información de los productos almacenados en el archivo 'stock.csv'.
    """
    for nombre, código, precio, stock in obtener_productos():
        print(f'Nombre: {nombre}')
        print(f'Código: {código}')
        print(f'Precio: {precio}')
        print(f'Stock: {stock}\n')

def agregar_producto(producto_nuevo: dict):
    """
    Agrega un nuevo producto al archivo 'stock.csv' con la información proporcionada en el diccionario producto_nuevo.
    """
    nombre = producto_nuevo['nombre']
    código = str(producto_nuevo['código'])
    precio = str(producto_nuevo['precio'])
    stock = str(producto_nuevo['stock'])
    producto = [nombre, código, precio, stock]
    with open('archivos/stock.csv', 'a', encoding='UTF-8') as stock_file:
        stock_file.write(f"\n{';'.join(producto)}")
        print('¡Producto agregado con éxito!')

def main():
    """
    Función principal que agrega dos productos, imprime la lista de productos y sus detalles.
    """
    producto_1 = {
        "nombre": "Cuaderno tamaño A4",
        "código": 35663,
        "precio": 550,
        "stock": 60
    }

    producto_2 = {
        "nombre": "Papel bond tamaño carta",
        "código": 35667,
        "precio": 620,
        "stock": 50
    }

    agregar_producto(producto_1)
    agregar_producto(producto_2)
    imprimir_productos()

main()