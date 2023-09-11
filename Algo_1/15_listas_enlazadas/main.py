def main():
    from listas_enlazadas import ListaEnlazada
    from iteradores import IteradorListaEnlazada

    L = ListaEnlazada()
    L.append('a')
    L.append('b')
    L.append('c')

    # Recorriendo la lista L
    it = IteradorListaEnlazada(L)
    while not it.está_al_final():
        print(it.dato_actual())
        it.avanzar()

main()