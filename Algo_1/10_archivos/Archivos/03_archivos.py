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

# Función 'compras' para manejar la creación de una lista de compras en un archivo 'compras.txt'.
def compras():
    with open('archivos/compras.txt', 'w') as archivo:
        # Solicita al usuario que ingrese productos para agregar a la lista de compras.
        producto = input('¿Qué agrego a la lista de compras?\n')
        
        # Mientras el usuario no ingrese 'X' en mayúsculas, se agregan productos a la lista y se escriben en el archivo.
        while producto.upper() != 'X':
            archivo.write(f'{producto}\n')  # Escribe el producto en el archivo de compras.
            producto = input('¿Qué agrego a la lista de compras?\n')  # Solicita el siguiente producto.

        # Indica que se ha completado la creación del archivo de compras cuando se ingresa 'X'.
        print(f'¡Archivo "{archivo.name}" creado con éxito!')

# Función principal que llama a la función 'compras' para crear la lista de compras.
def main():
    compras()

# Ejecución principal: llama a la función 'main' para iniciar el proceso de creación de la lista de compras.
main()