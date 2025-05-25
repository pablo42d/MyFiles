# # #zad 1
#
# def komunikat():
#     print("Hello Word")
#
# komunikat()
#
# #zad 1a
#
# def komunikat1(a):
#         print(a)
#
# a = "Hello Word"
#
# komunikat1(a)

# #zad 2
#
#
# def srednia(A,B):
#     suma = 0
#     ilosc = 0
#
#     while A <= B:
#         A += 1
#         ilosc += 1
#         suma += A
#         print(A)
#         print(suma / ilosc)
#
#
# A = 500
# B = 1000
# srednia(A,B)


# # zad 3
#
# x = 0
# y = 1
# z = int(input("podaj cyfre: "))
# a = 1
#
# def test(a,z):
#     if a <= z:
#         print(a)
#         test(a + 1,z) #pentla bez pentli do wartości z
#
# test(a,z)
#
# print("---------------------------zadanie 3a -------------------------")
# test(4,z)




## inne ciekawe
# a = 0
# while a < 10:
#     print(a)
#     a += 2  # a = a + 1  # a++ !!!Inkrementacja!!

# print("__________________________")
# import math
#
# for i in range(5, 10, 2):
#     print(i, math.pi)
#
#
# def fibbonaci(a):
#     if a == 1:
#         return 1
#     elif a == 2:
#         return 1
#     else:
#         return fibbonaci(a - 2) + fibbonaci(a - 1)
#
#
# for i in range(1, 10):
#     print(fibbonaci(i))

# zad 4
# def silnia(a):
#     if a == 1:
#         return 1
#     else:
#         return a * silnia(a - 1)
#
# print(silnia(6))
#
# #zad 5
#
#
# def czy_parzysta(a):
#     if a % 2 == 0:
#         print("jest parzysta")
#     else:
#         print("nie jest parzysta")
#
# czy_parzysta(6)
#
# #print("_____________________________zadanie 5b___________________________________")
# def czy_parzysta(a):
#     if a % 2 == 0:
#         return "jest parzysta"
#     else:
#         return "nie jest parzysta"
#
# for i in range(10):
#     print(i)
#
# b = int(input("podaj liczbę dolnego zakresu: "))
# c = int(input("podaj liczb górnego zakresu: "))
#
# for i in range(b, c):
#     wynik = czy_parzysta(i)
#     print(i, wynik)
#
#
# print("_____________________________zadanie 6 kalkulator___________________________________")
#
#
# def dodawanie(b, c):
#     return b + c
#
# def odejmowanie (b, c):
#     return b - c
#
# def dzielenie(b, c):
#     return b / c
#
# def potęgowane(b, c):
#     return b ** c
#
#
# while True:
#     print(" + dodawanie; " " - odejmowanie; " " / dzielenie; " " ** potęgowanie; ""q - wybierz aby zakończyć działanie kalkulatora")
#     wybor = input("Jakie działanie chcesz wykonać:")
#
#     if wybor in ["+", "-","/","**",]:
#         try:
#             b = int(input("Podaj pierwsą liczbę: "))
#             c = int(input("Podaj drugą liczbę: "))
#         except ValueError:
#             print("Błąd: wpisz poprawne liczby!")
#             continue
#
#
#     if wybor == "+":
#         print("Wynik dodawania to:", dodawanie(b,c))
#         print(
#         )
#
#     elif wybor == "-":
#         print("Wynik odejmowania to:", odejmowanie(b,c))
#         print(
#         )
#
#     elif wybor == "/":
#         print("wynik dzielenia to:", dzielenie(b,c))
#         print(
#         )
#
#     elif wybor == "**":
#         print("Wynik potęgowania:", potęgowane(b,c))
#         print(
#         )
#
#     elif wybor == "q":
#         print(
#         )
#         print("Kalkulator zakończył działanie")
#         break











#print("_____________________________zadanie 7___________________________________")

#
# b = input("Podaj liczbę binarną: ")
# a = str(b)
# a = reversed(a)
# suma = 0
# potega = 0
#
# for i in a:
#
#     suma += int(i) * (2 ** potega)  # Każda cyfra binarna mnożona przez odpowiednią potęgę 2
#     potega += 1
#     print(int(i))
#
# print("Liczba dziesiętna:", suma)

#print("_____________________________zadanie 8___________________________________")
#
# def czy_pierwsza(a):
#     if a < 2:
#         return "nie jest pierwsza"
#     for i in range(2, a):
#         if a % i == 0:
#             return "nie jest pierwsza"
#     return "jest pierwszą"
#
#
# b = int(input("podaj liczbę dolnego zakresu: "))
# c = int(input("podaj liczb górnego zakresu: "))
#
# for i in range(b, c):
#     wynik = czy_pierwsza(i)
#     print(i, wynik)

#print("_____________________________zadanie 9___________________________________")

# def liczba_cyfr(liczba):
#     liczba = abs(liczba)
#     return len(str(liczba))
# print(liczba_cyfr(2803))

# #print(-------my code-------)
#
#
# def licz_cyfry(liczba):
#     return len(str(liczba))
#
# #print(licz_cyfry(1234))
#
# liczba = input("Wprowadź liczbę całkowitą nieujemną: ")
# print(licz_cyfry(liczba))



#print("_____________________________zadanie 10___________________________________")

# tab = [1, 4, -4, 7]
# b = max(tab)
# n = len(tab)
# print("Sprawdzana tablica:", tab)
# print("Maksymalna wartość na liście:", b)
# print("Ilość elementów w tablicy", n)

# print("--------------------------------------------------")
# def f_tablica(tab,n):
#     b = max(tab)
#     # print("Maksymalna wartość na liście", b)
#     #
#     n = len(tab)
#     # print("Ilość elementów w tablicy",n)
#     return b
#
# tablica = [1, 4, -4, 7]
# n = len(tablica)
# wynik = f_tablica(tablica, n)
# print("Maksymalna wartość w tablicy to:", wynik)
#
# print("-------------------------------------------------------")
# def maks(tab):
#     b = max(tablica)
#     # print("Maksymalna wartość na liście", b)
#     return b
#
# def ilość(n):
#     n = len(tablica)
#     # print("Ilość elementów w tablicy",n)
#     return n
#
# tablica = [1, 4, -4, 7, 20]
#
# print(tablica)
# print("Maksymalna wartość na liście:", maks(tablica))
# print("Ilość elementów w tablicy:", ilość(tablica))

# print("------------------------iteracja po n ilości elementów---------------------")
#
# tablica = [1, 4, -4, 7, 3, 20, 105, 2]
# print(tablica)
# print("Wszystkich elementów w tablicy", len(tablica))
# n = int(input("Podaj liczbę elementów: "))
#
# def f_tablica(tab,n):
#
#     b = tab[0]
#     for i in range(n):
#         if tab[i] > b:
#             b = tab[i]
#     return b
#
#
# # n = 6
# wynik = f_tablica(tablica, n)
# print("Maksymalna wartość w tablicy dla ilości elementów", n, "to:", wynik)