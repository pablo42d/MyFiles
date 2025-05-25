import random


def generujTablice(n):
    # tab = random.sample(range(3, 100, 3), min(n, 10))
    tab = []
    for i in range(n):
        tab.append(random.randrange(3,31,3))

    return tab

def przeszukaj(tab):
    tab2 = []
    for j in tab:
        if j % 3 == 0:
            tab2.append(j)
        elif j % 5 == 0:
            tab2.append(j)
        elif j % 6 == 0:
            tab2.append(j)

    return tab2

n = int(input("Wprowadź wielkość tablicy: "))

losowaTablica = generujTablice(n)
print("Tablica wypełniona n lasowymi liczbami z przedziału 3-31 z wielokrotnością 3:", losowaTablica)

podzielne = przeszukaj(losowaTablica)
print("Nowa tablica z liczbami podzielnymi przez 3, 5, 6 to:", podzielne)

sumaTab = losowaTablica + podzielne
print("Suma tablic:", sumaTab)

print("Ile elementów w tablicy:", len(sumaTab))
print("Minimalna liczba w tablicach:", min(sumaTab))
print("Maksymalna wygenerowana wielokrotnośc liczby 3 w tablicach to:", max(sumaTab))


