# zad.1

# x = "Hello World"  # Użycie cudzysłowu, aby oznaczyć ciąg tekstowy
# print(x)  # Wyświetlenie wartości zmiennej a
#
# x = input("Hello World")
# print(x)

# zad.2

# a = 2
# b = 3
# print(a+b)  # Wyświetlenie Wyniku

# zad.3

#Wczytanie danych od użytkownika
# imie = input("Podaj swoje imię: ")
# nazwisko = input("Podaj swoje nazwisko: ")
# wiek = int(input("Podaj swój wiek: "))  # Konwersja na liczbę całkowitą
# cena_chleba = float(input("Podaj cenę chleba: "))  # Konwersja na liczbę zmiennoprzecinkową

#Wyświetlenie wczytanych danych
#print(imie)
#print(nazwisko)
#print(wiek)
#print(cena_chleba)
#lub
# print("\nPodane dane:")
# print(f"Imię: {imie}")
# print(f"Nazwisko: {nazwisko}")
# print(f"Wiek: {wiek}")
# print(f"Cena chleba: {cena_chleba} zł")  # Wyświetlenie ceny bez wymuszonego formatowaniap
#lub
#print(f"Cena chleba: {cena_chleba:.2f} zł")  # Wyświetlenie ceny z dokładnością do 2 miejsc po przecinku

#zad.4
#
# def funkcja2(): # zad.2
#     a = 2
#     b = 3
#     print(a+b)  # Wyświetlenie Wyniku
#
# def funkcja3(): #zad.3
#     imie = input("Podaj imię: ")
#     nazwisko = input("Podaj nazwisko: ")
#     wiek = int(input("Podaj wiek: "))  # Konwersja na liczbę całkowitą
#     cena_chleba = float(input("Podaj cenę chleba: "))  # Konwersja na liczbę zmiennoprzecinkową
#
#     print(imie)
#     print(nazwisko)
#     print(wiek)
#     print(cena_chleba)
#
#
# def funkcja1(): #zad.1
#     print("Hello world")
#
# wybor=int(input("Wybierz opcje"))
# print(wybor)
#
# if wybor==1:
#     funkcja1()
#
# if wybor==2:
#     funkcja2()
#
# if wybor==3:
#     funkcja3()

#zad.5

# def pole_prostokata(a, b):
#     return a * b
#
# a = float(input("Podaj wartość boku a: "))
# b = float(input("Podaj wartość boku b: "))
# c = "Obliczone pole prostokąta to: "
# pole = pole_prostokata(a, b) #wywołanie funkcji def pole_pros...
#
# print(c, pole)

# zad.6

# import math
#
#
# def pole_powierzchni_walca(r, h):
#     pp = math.pi * r**2
#     pb = 2 * math.pi * r * h
#     return 2 * pp * pb
#
# def objętośc_walca(r, h):
#     return math.pi * r**2 * h
#
#
# h = float(input("Podaj Wysokość:"))
# r = float(input("Podaj promeń:"))
# p = "Obliczone pole powierzchni:"
# v = "Obliczona objętość:"
# if r < 0 or h < 0:
#     print('Wprowadż wartość dodatnią !!!')
#
#
# else:
#     print(p, pole_powierzchni_walca(r, h))
#     print(v, objętośc_walca(r, h))

#zad.7

# def suma(a, b):
#     return a + b
#
# a = int(input("Podaj liczbę a:"))
# b = int(input("Podaj liczbę b to:"))
# suma = "Suma liczb a i b:"
# d = "Potrójna suma wartość gdy a równe b to: "
# if a==b:
#     print(d, (a+b)*3)
# else:
#     print(suma, a+b)

#zad.8

# for i in range (1,101):
#    print(i)

#zad.9

# import random
#
# a = [random.randint(1, 100) for _ in range(5)]
# print("Wygenerowane losowo 5 liczby z zakresu 1-100 to:", a)

#zad.10

# list = [1,4,-4,7]
#
# a = min(list)
# b = max(list)
#
# print("Sprawdzana lista:",list)
# print("Minimalna wartość na liście:", a)
# print("Maksymalna wartość na liście:", b)

#zad.12

#
# operator = input("Wprowadź operator arytmetyczny ( + , - , * , / ): ")
# liczba1 = float(input("Wprowadź pierwszą liczbę: "))
# liczba2 = float(input("Wprowadź drugą liczbę: "))
# wynik = "Wynik obliczeń to: "
#
# if operator == "+":
#     print("Wynik dodawania to: ", (liczba1 + liczba2))
#
# elif operator == "-":
#     print(wynik, (liczba1 - liczba2))
#
# elif operator == "*":
#     print(wynik, (liczba1 * liczba2))
#
# elif operator == "/":
#     print(wynik, (liczba1 / liczba2))
#

#zad.13

#
# while True:
#     try:
#         liczba=int(input("Wprowadź liczbę: "))
#
#         if liczba < 10:
#             print("Ta liczba jest za mała:")
#         else:
#             print( "Ta liczba jest wystarczająco duża")
#             break
#
#     except :
#         print("Niewłaściwe dane. Wprowadż liczby całkowite.")
#

#zad.15

# def fibonacci(n):
#     """Generuje pierwsze n liczb ciągu Fibonacciego."""
#     fib_sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence
#
# # Pobieranie danych od użytkownika
# while True:
#     try:
#         liczba = int(input("Podaj, ile liczb ciągu Fibonacciego wygenerować: "))
#         if liczba <= 0:
#             print("Podaj liczbę większą od zera.")
#         else:
#             break
#     except ValueError:
#         print("Nieprawidłowy format. Podaj liczbę całkowitą.")
#
# # Generowanie i wypisywanie ciągu Fibonacciego
# wynik = fibonacci(liczba)
# print(f"Pierwsze {liczba} liczb ciągu Fibonacciego to: {wynik}")
#


