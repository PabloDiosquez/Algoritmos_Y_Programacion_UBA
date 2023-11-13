# En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
# cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
# es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
# cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta
# forma:

# Agus
# Manu
# Santi
# Lorena
# Maria

# La función tiene que devolver 5000
# c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
# de los nombres, se agregue también a Tomi.

# Función para obtener los nombres de un archivo 'regalo.txt'.
def obtener_nombres():
    with open('archivos/regalo.txt', 'r') as nombres:
        # Lee los nombres del archivo, eliminando espacios en blanco alrededor de cada nombre.
        return [nombre.strip() for nombre in nombres.readlines()]

# Función para escribir un nombre en el archivo 'regalo.txt' si se cumple una condición.
def escribir_nombre_si(nombre: str, condición: bool):
    if condición:
        with open('archivos/regalo.txt', 'a') as nombres:
            # Agrega un nombre al archivo si se cumple la condición y muestra un mensaje de éxito.
            nombres.write(f'\n{nombre}')
            print(f'Se ha agregado a {nombre} a "{nombres.name}" con éxito!')
    # Devuelve la lista actualizada de nombres.
    return obtener_nombres()

# Función para calcular el dinero total recaudado basado en la cantidad de nombres.
def obtener_dinero_total(nombres: list):
    # Calcula el dinero total multiplicando la cantidad de nombres por $1000.
    return len(nombres) * 1000

# Función principal que coordina todas las operaciones.
def main():
    # Obtiene los nombres actuales desde el archivo.
    nombres = obtener_nombres()
    # Agrega el nombre 'Tomi' al archivo si 'Santi' está presente en los nombres.
    nombres = escribir_nombre_si('Tomi', 'Santi' in nombres)
    # Imprime los nombres de los participantes en el regalo de Sol.
    print('Participantes del regalo de Sol:')
    for nombre in nombres:
        print(nombre)
    # Calcula y muestra el dinero total recaudado para el regalo de Sol.
    print(f'Dinero total recaudado para Sol: ${obtener_dinero_total(nombres)}')

# Ejecuta la función principal para realizar todas las operaciones.
main()