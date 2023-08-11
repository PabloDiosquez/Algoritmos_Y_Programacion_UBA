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
          
def miki_moko(n: int):
    for i in range(1, n+1):
        if not i % 3 and not i % 5: print("MikiMoko")
        elif not i % 3:             print("Miki")
        elif not i % 5:             print("Moko")
        else:                       print(i)

miki_moko2()
# miki_moko(100)
