# Condicionales 🐱‍🚀

def miki_moko1():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0: 
            print("Miki")
        if i % 3 != 0 and i % 5 == 0:
            print("Moko")
        if i % 3 == 0 and i % 5 == 0:
            print("MikiMoko")
        if i % 3 != 0 and i % 5 != 0:
            print(i)

def miki_moko2():
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("MikiMoko")
            else:
                print("Miki")
        else: # no es divisible por 3 
            if i % 5 == 0:
                print("Moko")
            else: 
                print(i) 

def miki_moko3():
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("MikiMoko")
            else:
                print("Miki")
        elif i % 5 == 0:
            print("Moko")
        else:
            print(i)

def miki_moko4():
    for i in range(1, 101):
        print(_miki_moko4(i))

def _miki_moko4(i: int):
        if i % 3 == 0:
            if i % 5 == 0:
                return "MikiMoko"
            return "Miki"
        elif i % 5 == 0:
            return "Moko"
        return i
          
def miki_moko(n: int):
    for i in range(1, n+1):
        if not i % 3 and not i % 5: print("MikiMoko")
        elif not i % 3:             print("Miki")
        elif not i % 5:             print("Moko")
        else:                       print(i)

# miki_moko4()
# miki_moko(100)

# Bonus track ☂ 
# Instrucción assert 
def factorial(n: int) -> int:
    """ Describe el factorial del número dado.
    """
    if n == 0: return 1
    return factorial(n-1)*n 

# if + return 
def es_par(n: int) -> bool:
    "Indica si el número dado es par."
    return not n % 2  

def casos_de_prueba():
    # factorial()
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    # es_par()
    assert es_par(0)
    assert not es_par(1)
    assert es_par(2)
    assert not es_par(3)
    assert es_par(4)
    assert not es_par(5)

casos_de_prueba()