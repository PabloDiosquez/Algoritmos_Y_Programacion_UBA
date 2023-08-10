# Condicionales 🐱‍🚀

def miki_moko(n: int):
    for i in range(1, n+1):
        if not i % 3 and not i % 5: print("MikiMoko")
        elif not i % 3:             print("Miki")
        elif not i % 5:             print("Moko")
        else:                       print(i)

# miki_moko(100)