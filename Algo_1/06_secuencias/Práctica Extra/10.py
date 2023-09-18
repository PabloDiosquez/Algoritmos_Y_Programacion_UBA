# 10.
def crear_pais():
    """
    Crea un país.
    Retorna:
    tuple: Una tupla con el nombre, la capital y el continente del país.
    """
    nombre     = input("Nombre: ")
    capital    = input("Capital: ")
    continente = input("Continente: ")
    return (nombre, capital, continente)

def agregar_pais_a_lista(paises: list, pais: tuple):
    """
    Agrega el país dado a la lista de países dada.
    Parámetros:
    paises (list): La lista de países a la que se va a agregar el país.
    pais (tuple): Una tupla con el nombre, la capital y el continente del país.
    """
    paises.append(pais)

def info_paises(paises: list):
    """
    Recorre la lista de países 'paises' e imprime la información de los mismos.
    Parámetros:
    paises (list): La lista de países de la que se imprimirá la información.
    """
    for pais in paises:
        print(f"Nombre: {pais[0]}")
        print(f"Capital: {pais[1]}")
        print(f"Continente: {pais[2]}")
        print(" ▪ "*10) 

def main():
    paises = []
    # Ejemplo 1
    pais1 = crear_pais()
    agregar_pais_a_lista(paises, pais1)
    # Ejemplo 2
    pais2 = crear_pais()
    agregar_pais_a_lista(paises, pais2)
    # Ejemplo 3
    pais3 = crear_pais()
    agregar_pais_a_lista(paises, pais3)
    # Ejemplo 4
    info_paises(paises)
    # Ejemplo 5
    pais4 = crear_pais()
    agregar_pais_a_lista(paises, pais4)
    # Ver información de los países
    info_paises(paises)

if __name__ == "__main__":
    main()