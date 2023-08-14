#¿Cuántas letras 'o' tiene 'Los Orozco'?
 
LETRA_OROZCO ="""
Nosotros no somos como los Orozco
Yo los conozco, son ocho los monos:
Pocho, Toto, Cholo, Tom
Moncho, Rodolfo, Otto, Pololo
Yo pongo los votos sólo por Rodolfo
Los otros son locos, yo los conozco, no los soporto
Stop. Stop
Pocho Orozco:
Odontólogo ortodoxo, doctor
Como Borocotó
Oncólogo jodón
Morocho tordo
Groncho jocoso
Trosko
Chocó con los montos
Colocó Molotov. Bonzo
Toto Orozco:
Colocón
Drogón como pocos
Tomó todos los hongos
Monologó solo como por dos otoños
Botó formol por los ojos
Tomó cloroformo, bols, ron, porrón, torronto, toso
Norto con Bordón
¿Lo votó o no?
Dobló los codos como loco
¡¡Coño! ¿sos vos Toto?
Corroboró
Socorro, cómo tomó
Morfó hot dog, mondongo, pollo con porotos
Lloró, lloró con dolor
Por como lloró tomó como dos hongos
Tocó fondo
Torró como loco
Contó todo, todo, todo
Bochornoso como Cóppolo. Stop. Stop
Cholo Orozco:
Mocoso
Soplón
Moroso
Bocón
Chorro como Grosso
Robó dos potros por Comodoro
Los montó, los trotó por Bolsón
Por los Toldos
Por Chocón
Doloroso. Stop. Stop
Tom Orozco:
Proctólogo morboso
Compró por los shops fotos porno color
Compró como dos tomos
Trozos
Cosos
Colchón roto
Homós como Gomón
Trolos gozosos con condón
Pomos con moño rococó
Todos polvos cortos
Fogoso. Stop. Stop
Nosotros no somos como los Orozco
Yo los conozco, son ocho los monos:
Pocho, Toto, Cholo, Tom
Moncho, Rodolfo, Otto, Pololo
Yo pongo los votos sólo por Rodolfo
Los otros son locos, yo los conozco, no los soporto
Stop. Stop
Moncho Orozco:
Sólo probó porro
Voló con los ojos rojos por los polos
Voló por Bonn, voló por Hong Kong
Por London, soñó con Yoko Ono, lloró por John
Voló por vos
Voló por nosotros
Brotó como flor bordó
Roló pot, nos contó
Los tronchos son grosos como los corchos
Bocho borroso. Stop. Stop
Rodolfo Orozco:
Con voz como John Scott
Ronco, ronco
Formó todos los coros
Tocó: Doblo con Mollo, bombo con Moro
Tom tom con Porno, joropo con Tormo, bongó con Don Johnson
Tocó con Toto, los Lobos, los Door, los Moscos
Compró dos vox
Tocó "Socorro" con Pol
Nos contó con honor: ¡Toco con Bob! ¡Toco con Bob!
Sopló corno, trombón
Tocó son sonoro con los cocos
Rock, pop, folk, pogo
Nos contó como oyó todos los: ¡¡Oh, oh, oh, oh, oh...!
Tocó con todos
Por poco no tocó con Colón
Coloso. Stop. Stop
Otto Orozco:
Con otros rollos
Con poco protocolo
Copó todo como los Born, Troncoso, Don Floro o los Lococo
Logró otro comfort
Ojo por ojo
Controló todo
Convocó por fono los otros Orozco
Contó con todos
Cobró todos los bonos
Bocón
Colocó montos grosos por Boston
Cobró dos lotos
Compró dos Ford, ocho Volvo, dos Gol
Oro
Motos
Toros
Compró los Coto, Rodó, Coconor
Zorro. Stop. Stop
Pololo Orozco:
Gordo fofo con olor
Mormón
Glotón con jopo
Rostro poroso
Rotoso
Como con motor roto
Solo como croto
Solo como topo
Solo como Don Bosco con poncho
Choto. Stop. Stop
"""

def cantidad_letras_o(letra: str):
    """ Describe la cantidad de letras 'o' en el string dado.
    """
    cantidad = 0
    # Recorremos con un ciclo todos los caracteres de la canción
        # Si es una 'o' ➡ cantidad = cantidad + 1
    for indice in range(len(letra)):
        if letra[indice] in 'oOóÓöÖ': cantidad += 1 # operador in 
    return cantidad 

def cantidad_en_de_letras__(texto: str, letra: str) -> int:
    """ Describe la cantidad de letras 'letra' en el texto dado.
    """
    contador = 0
    for caracter in texto.lower():
        if caracter == letra: contador += 1
    return contador 

def es_numerico(cadena: str):
    """ Indica si todos los caracteres de la cadena son números enteros.
        Describe True si int(cadena) funciona.
    """
    if es_vacía(cadena): return False # Caso borde

    NÚMEROS = "0123456789"
    for caracter in cadena:
        if caracter not in NÚMEROS: return False 
    return True 
    
def es_vacía(cadena: str):
    """ Indica si la cadena dada está vacía.
    """
    return not len(cadena)

def main():
    total = len(LETRA_OROZCO)
    cantidad_o = cantidad_letras_o(LETRA_OROZCO)
    mensaje = f"La letra de 'Los Orozco' tiene {cantidad_o} letras 'o' sobre un total de {total} caracteres." # interpolación de cadenas 
    print(mensaje)

    s = "python"                                                    # ➡ inmutables 
    print(type(s))

    t = (1, 2, 3.5, "esto es una cadena de caracteres", (1, 2, 3))  # ➡ inmutables
    print(type(t))

    L = [1, 2, 3.5, "esto es una cadena de caracteres", (1, 2, 3)]  # ➡   mutables
    print(type(L))  

    # Slices 🐸

    # Los slices en Python son una forma conveniente de obtener una porción o subconjunto de elementos de una secuencia, como una lista, una cadena de caracteres o una tupla. Se definen utilizando la sintaxis [inicio:fin:paso], donde:

    # inicio es el índice de inicio del slice (inclusive).
    # fin es el índice de fin del slice (exclusivo).
    # paso es el tamaño del salto entre elementos (opcional).

    lista = [1, 2, 3, 4, 5]
    sl1 = lista[1:4]  # Obtiene [2, 3, 4]
    sl2 = lista[:3]   # Obtiene [1, 2, 3]
    sl3 = lista[2:]   # Obtiene [3, 4, 5]
    sl4 = lista[::2]  # Obtiene [1, 3, 5]

    # Pruebas sobre la función es_numerico()
    assert     es_numerico("345")  # True 
    assert not es_numerico("x345") # False 
    assert not es_numerico("")     # False 
    assert not es_numerico("3.5")  # False 

    # Matrices 🪓

    M = [[2, -1, 4], [5, 0, 2]] # Secuencia de columnas
    print(M[1][1]) # 0

main()