#
# tab=[]
# a=1
# b=2
# c=4
# tab=[a,b,c,10,20]
# print (tab)
# tab.append("push")
# print (tab)
# print (tab[1])
# print (tab[-2])
# tab.append([0,1,11,111])
# print(tab[-1][1])

# # Zadanie 1:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(700)
# print(list1)
# #list1[2][2].insert(__index=1,)
#
# print(list1.pop())
# print(list1)

# # Zadanie 2:
#
# listaPotengowana=[]
# lista=[1,2,3,4,5]
# n=int(input("podaj pierwiastek"))
# for i in range(len(lista)):
#     print(lista)
# listaPotegowa =(i**n)
# print (listaPotegowa)

# # Zadanie 3:

# Napisz program, który doda dwie listy według indeksu, tak żeby lista1 i lista 2 pokazały logiczne zdanie:

#
# list1 = ["M", "n", "im", "Pio"]
# list2 = ["am", "a", "ie", "tr"]


# lista = []
# for i in range(len(list1)):
#     print(list1[i]+list2[i])
#     lista.append(list1[i]+list2[i])
# print(lista)

# # Zadanie 4:
# Przekształć dwie listy w słownik.

# list1 = ["M", "n", "im", "Pio"]
# list2 = ["am", "a", "ie", "tr"]

# slownik = dict(zip(list1,list2))
# print(slownik)

# # Zadanie 5:
# Połącz dwa słowniki Pythona w jeden.

# dict1 = {"M": "am","n":"a" }
# dict2 = {"im":"ie" , "Pio" : "tr"}


# dict0 = {**dict1, **dict2}

# print(dict0)


# # Zadanie 6:

# Wyświetl na konsoli wartość klucza „history” z poniższego:
# slownik = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80 } } } }

# slownik = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80 } } } }

# print(slownik)
# print(slownik["class"])
# print(slownik["class"]["student"])
# print(slownik["class"]["student"]["marks"]["history"])
# slownik["class"]["student"]["marks"]["history"]=66
# print(slownik)


# Zadanie 7:
# Napisz funkcję, która przyjmuje wartość temperatury w Kelvinach i zwraca wartość wyrażoną w stopniach Celsjusza: TC = TK − 272.15.W przypadku podania wartości ujemnej funkcja zwraca None.Przetestuj jej działanie.
# tk = float(input("Podaj temperaturę w Kelvinach: "))
#
#
# def kelviny(tk):
#     if tk < 0:
#         return None
#
#     return tk - 273.15
#
#
# tc = kelviny(tk)
#
# print(tk, "K =", tc, "°C")

# Zadanie 8:
# Stwórz funkcję, która rysuje choinkę. Program powinien zawierać funkcję, przyjmującą parametr, określający wielkość choinki.

# def choinka(wielkosc):
#     for i in range(wielkosc):
#         print(" "*(wielkosc - i),"*"*((i*2) -1))

# def pien(n):
#     for i in range(n):
#         print(" "* (n + 6), "+"*(2))

# def land(n):
#     for i in range(1):
#         print("_"*(i + 30))


# choinka(10),pien(1),land(15)

# # Zadanie 9:

# Napisz program  wypisujący 10 liczb w jednym wierszu.

# import random

# def wypelnijLosowo(n=100):
#     tab=[]
#     for i in range(n):
#         tab.append(random.randint(1,11))
#     return tab
# x = wypelnijLosowo(10)
# print(x)

# # Zadanie 10:
# Napisz program rysujący macierz wypełnioną kolejnymi,  liczbami naturalnymi od 0. Program powinien zawierać funkcję, która przyjmuje parametr określający rozmiar macierzy (np. 7x7 lub 12x12 …)


# def rysuj(n):

#     for i in range(1, n):
#         print(" ".join((str(i + j)for j in range(1, n))))


# n = 11
# rysuj(n)


# # Zadanie 11:

# Zmodyfikuj powyższy program program tak, aby wypisywał tabliczkę mnożenia.

# def rysuj(n):

#     for i in range(1, n):
#             print(" ".join((str(i * j)for j in range(1, n))))


# n = 11
# rysuj(n)


# # Zadanie 12:

# Napisz program, który posiada funkcję fillNie, wypełniającą tablicę o rozmiarze n (podanym przez użytkownika), liczbami losowymi, z zakresu od 1 do 10. Dodatkowo program musi posiadać funkcję wypisującą elementy tablicy na ekranie, w jednym wierszu oraz funkcję searchNie, wyszukującą wystąpienie liczby n, w wypełnionej tablicy.

# import random

# def wypelnijLosowo(n=100):
#     tab=[]
#     for i in range(n):
#         tab.append(random.randint(1,11))
#     return tab


# tablica = wypelnijLosowo(16)

# print(tablica)

# x = int(input("podaj liczbę: "))

# print("Liczba występuje w tablicy:", tablica.count(x), "razy")


# # Zadanie 13:
# Napisz program,  który w tablicy dwuwymiarowej 10×10 umieszcza losowo na przekątnej liczby od 1 do 10, a poza nią zera. Dodatkowo oblicza on sumę liczb znajdujących się na przekątnej. Program powinna zawierać trzy metody:
# generujDane() — umieszcza dane w tablicy,
# wyswietlWynik() — pokazuje zawartość tablicy na ekranie monitora.
# przetworzDane() — oblicza i wyświetla sumę liczb znajdujących się na przekątnej,


# import random

# def generujDane(n=11):
#     tab = []

#     for i in range(1, n):
#         tabTemp = []
#         for j in range(1, n):
#             if j == i:
#                 tabTemp.append(random.randint(1, 11))
#             else:
#                 tabTemp.append(0)
#         tab.append(tabTemp)
#     return tab


# x = generujDane(11)


# def wyswietlWynik():
#     for i in x:
#         print(i)


# wyswietlWynik()

# def przetworzDane():
#     suma = 0
#     for i in range(len(x)):
#         suma += x[i][i]  # Dodawanie elementów z przekątnej
#     print("Suma liczb na przekątnej:", suma)

# przetworzDane()


# # Zadanie 14:
# Napisz program,  który w tablicy dwuwymiarowej 10×10 umieszcza losowo na jednej części po przekątnej liczby od 0 do 9, wraz z przekątną, a poza nią zera.  Napisz funkcję, która odwraca tę macierz symetrycznie w osi przekątnej powstałej macierzy.

# import random
#
#
# def generujDane(n):
#     tab = []
#
#     for i in range(0, n):
#         tabTemp = []
#         for j in range(10):
#             if j <= i:
#                 tabTemp.append(random.randint(0, 9))
#             else:
#                 tabTemp.append(0)
#         tab.append(tabTemp)
#
#     return tab
#
#
# x = generujDane(10)
#
# # print(x)
#
# def wyswietlWynik():
#     for i in x:
#         print(i)
#
#
# wyswietlWynik()
#
# def odwroc(tab):
#
#     return [[tab[j][i] for j in range(len(tab))] for i in range(len(tab[0]))]
#
#
# def wyswietlWynik(tab):
#     for i in tab:
#         print(i)
#
#
#
# odwrocona = odwroc(x)
#
# print("Odwrócona:")
# wyswietlWynik(odwrocona)
# __________________________________________________________________________________________________________________________

# # Zad 10 GPT:

# def rysuj_macierz(rozmiar):
#     # Inicjalizujemy zmienną, która będzie przechowywać liczbę, którą wstawiamy do macierzy
#     liczba = 0
#
#     # Tworzymy macierz o zadanym rozmiarze
#     for i in range(rozmiar):
#         for j in range(rozmiar):
#             # Drukujemy kolejną liczbę i dodajemy spację dla lepszej czytelności
#             print(f"{liczba:3}", end=" ")
#             liczba += 1
#         # Po zakończeniu rysowania wiersza przechodzimy do nowej linii
#         print()
#
#
# # Przykład użycia funkcji
# rozmiar = int(input("Podaj rozmiar macierzy: "))  # Wczytujemy rozmiar od użytkownika
# rysuj_macierz(rozmiar)


# __________________________________________________________________________________________________________________________________

# na pamięć nauczyć się tego kodu
# Ctrl+b podpowiedz
# Wypełnia tablice losowymi liczbami
# import random

#
# def wypelnijLosowo(n=100):
#     tab=[]
#     for i in range(n):
#         tab.append(random.randint(1,11))
#     return tab
# x = wypelnijLosowo(6)
# print(x)

# _________________________________________________________________________________________________________________________________

# zad 14 gpt

# import random

# # Funkcja generująca tablicę 10x10
# def generuj_macierz():
#     # Tworzymy pustą tablicę 10x10 wypełnioną zerami
#     macierz = [[0 for _ in range(10)] for _ in range(10)]

#     # Umieszczamy liczby od 0 do 9 w jednej części po przekątnej
#     for i in range(10):
#         for j in range(i+1):
#             macierz[i][j] = random.randint(0, 9)

#     return macierz

# # Funkcja wypisująca macierz
# def wypisz_macierz(macierz):
#     for wiersz in macierz:
#         print(" ".join(map(str, wiersz)))

# # Funkcja odwracająca macierz symetrycznie względem przekątnej
# def odwracaj_macierz(macierz):
#     # Transponowanie macierzy
#     for i in range(10):
#         for j in range(i+1, 10):  # Tylko górna część, bo przekątna już jest na swoim miejscu
#             # Zamieniamy elementy symetrycznie względem przekątnej
#             macierz[i][j], macierz[j][i] = macierz[j][i], macierz[i][j]

# # Główna część programu
# if __name__ == "__main__":
#     # Generowanie macierzy
#     macierz = generuj_macierz()

#     print("Wygenerowana macierz:")
#     wypisz_macierz(macierz)

#     # Odwracanie macierzy
#     odwracaj_macierz(macierz)

#     print("\nMacierz po odwróceniu:")
#     wypisz_macierz(macierz)

