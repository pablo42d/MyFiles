
# # Lab1.1
# import math
# def wprowadz_dane(n):
#     while True:
#         try:
#             return float(input(n))  # Konwersja na liczbę rzeczywistą
#         except ValueError:
#             print("Wprowadzona wartość nie jest liczbą rzeczywista. Spróbuj jeszcze raz.")
#
# # Pobieranie danych od użytkownika
# a = wprowadz_dane("Podaj wartość dla a: ")
# b = wprowadz_dane("Podaj wartość dla b: ")
# c = wprowadz_dane("Podaj wartość dla c: ")
#
# # Funkcja rozwiązująca równanie kwadratowe
# def Oblicz(a, b, c):
#     if a == 0:
#         print("To nie jest równanie kwadratowe, ponieważ a = 0")
#     else:
#         d = b ** 2 - 4 * a * c
#
#         # Sprawdzenie, w zależności od wartości delty
#         if d > 0:
#             # Dwa różne pierwiastki rzeczywiste
#             x1 = (-b + math.sqrt(d)) / (2 * a)
#             x2 = (-b - math.sqrt(d)) / (2 * a)
#             print(f"Pierwiastki równania to: x1 = {x1}, x2 = {x2}")
#
#         elif d == 0:
#             # Jeden pierwiastek podwójny
#             x = -b / (2 * a)
#             print(f"Pierwiastek podwójny równania to: x = {x}")
#
#         else:
#             # Brak pierwiastków rzeczywistych
#             print("Brak pierwiastków rzeczywistych.")
#
# # Rozwiąż równanie kwadratowe
# Oblicz(a, b, c)

# # Lab1.2
# # V_1

# # Funkcja wczytująca n liczb i licząca liczby parzyste
# def licz_parzyste(n,a,d):
#     ile_parzystych = 0  # Inicjalizujemy licznik liczb parzystych
#     print("Licznik parzystyczh", ile_parzystych)
#     for i in range(n):
#         generuj_ciąg = a + i * d
#         print(generuj_ciąg)
#         if generuj_ciąg % 2 == 0:
#             ile_parzystych += 1
#     print(f"Liczba liczb parzystych w ciągu n: {ile_parzystych}")  # Wyświetlenie wyniku
#
# # Wczytanie długości ciągu
# n = int(input("Podaj liczbę n (długość ciągu): "))
# a = int(input("Podaj liczbę a (liczba): "))
# d = int(input("Podaj liczbę d (zwiększ o a + d): ")) # zwiększa wartość w ciągu o zadaną wrtość d
# # Wywołanie funkcji liczącej liczby parzyste
# licz_parzyste(n,a,d)

# V_3
# def count_even_numbers():
#     # Wczytanie wartości n
#     n = int(input("Podaj n liczbę elementów w ciągu (n > 0): "))
#
#     for i in n:
#         if n <= 0:
#             print("Spróbuj jeszcze raz: n musi być większe od zera!")
#             return
#
#     liczba_liczb_parzystych = 0  # Licznik liczb parzystych
#
#     for liczba in range(n):
#         wprowadzona = int(input(f"Podaj liczbę {liczba + 1}: "))  # Wczytanie liczby
#         if wprowadzona % 2 == 0:
#             liczba_liczb_parzystych += 1  # Jeśli parzysta, +1
#
#     print(f"Liczba parzystych liczb w ciągu: {liczba_liczb_parzystych}")
#
#
# # Uruchomienie funkcji
# count_even_numbers()


# # V_4
# def ile_parzystych():
#     # Pętla, aby wymusić poprawne wprowadzenie `n`
#     while True:
#         try:
#             n = int(input("Podaj liczbę elementów w ciągu (n > 0): "))
#             if n > 0:
#                 break  # Poprawne `n`, wychodzimy z pętli
#             else:
#                 print("liczba musi być większa od zera! Spróbuj ponownie.")
#         except ValueError:
#             print("Wprowadź poprawną liczbę całkowitą!")
#
#     licz_parzyste = 0  # Licznik liczb parzystych
#
#     for i in range(n):
#         while True:
#             try:
#                 liczba = int(input(f"Podaj liczbę {i + 1}: "))
#                 break  # Poprawna liczba, wychodzimy z pętli
#             except ValueError:
#                 print("Błąd: Wprowadź poprawną liczbę całkowitą!")
#
#         if liczba % 2 == 0:
#             licz_parzyste += 1  # Jeśli parzysta, zwiększamy licznik
#
#     print(f"Liczba parzystych liczb w ciągu: {licz_parzyste}")
#
#
# # Uruchomienie funkcji
# ile_parzystych()


# # V_5
# # Pobranie liczby n od użytkownika
# n = int(input("Podaj liczbę n: "))
#
# # Jeśli n == 0, ustaw na 1
# if n == 0:
#     n = 1
#
# # Zmienna przechowująca liczbę parzystych
# liczba_parzysta = 0
#
# # Iteracja dla liczb od 1 do n
# for liczba in range(1, n + 1):
#     # Sprawdzenie czy liczba jest parzysta
#     if liczba % 2 == 0:
#         liczba_parzysta += 1
#
# # Wypisanie wyniku
# print("Liczba parzystych:", liczba_parzysta)


# # Funkcja wczytująca n liczb i licząca liczby parzyste
# def licz_parzyste(n):
#     licznik_parzystych = 0  # Inicjalizujemy licznik liczb parzystych
#     for i in range(n):
#         liczba = int(input(f"Podaj liczbę {i+1}: "))  # Wczytanie liczby
#         if n
#         if liczba % 2 == 0:  # Sprawdzenie, czy liczba jest parzysta
#             licznik_parzystych += 1  # Zwiększenie licznika parzystych
#     print(f"Liczba liczb parzystych: {licznik_parzystych}")  # Wyświetlenie wyniku
#
# # Wczytanie długości ciągu
# n = int(input("Podaj liczbę n (długość ciągu): "))
#
# # Wywołanie funkcji liczącej liczby parzyste
# licz_parzyste(n)


# # V_6
# def licz_parzyste():
#     # Wczytywanie (długość ciągu) n, aż będzie > 0
#     while True:
#         try:
#             n = int(input("Podaj liczbę liczb w ciągu (n > 0): "))
#             if n > 0:
#                 break
#             else:
#                 print("Liczba elementów musi być większa od zera! Spróbuj ponownie.")
#         except ValueError:
#             print("Wprowadź poprawną liczbę całkowitą!")
#
#     parzysta = 0  # Licznik parzystych
#
#     # Wczytywanie n liczb i sprawdzanie parzystości
#     for i in range(n):
#         while True:
#             try:
#                 liczba = int(input(f"Podaj liczbę {i + 1} dla ciągu: "))
#                 break
#             except ValueError:
#                 print("Wprowadź poprawną liczbę całkowitą!")
#         if liczba % 2 == 0:
#             parzysta += 1
#     return parzysta
#
# # Wywołanie funkcji
# x = licz_parzyste()
# print("Liczba parzystych elementów w ciągu:", x)

# # Zad_3
#
# # 1. Wczytanie liczby n i sprawdzenie warunku
# n = int(input("Podaj liczbę elementów w ciągu (n > 0): "))
# if n <= 0:
#     print("Liczba n musi być większa od 0!")
#     exit()
#
# # 2. Wczytanie n liczb i zapisanie ich w liście
# ciag = []
# print(ciag)
# for i in range(n):
#     liczba = int(input(f"Podaj liczbę {i + 1}: "))
#     ciag.append(liczba)
#     print(liczba)
# print(ciag)
#
#
# # 3. Wczytanie liczby do wyszukania
# x = int(input("Podaj liczbę do wyszukania: "))
#
# # 4. Sprawdzenie, czy liczba x występuje w ciągu
# if x in ciag:
#     indeks = ciag.index(x)  # Pierwsze wystąpienie
#     print(f"Liczba {x} występuje w ciągu na indeksie {indeks}.")
# else:
#     print(f"Liczba {x} nie występuje w ciągu.")
#
#
# # Zad_4
#
# import random
#
# def graj():
#     # Wybór losowej liczby z zakresu 1-100
#     wylosowana_liczba = random.randint(1, 100)
#     ile_prob = 1
#     print("Zgadnij liczbę z zakresu od 1 do 100!")
#
#     while True:
#         jaka_liczba = int(input(f"Próba {ile_prob}: Podaj swoją liczbę: "))
#
#         if jaka_liczba == wylosowana_liczba:
#             print(f"Gratulacje! Odgadłeś liczbę {wylosowana_liczba} w {ile_prob} próbach.")
#             break  # Przerwanie pętli, gdy liczba została odgadnięta
#
#         elif jaka_liczba > wylosowana_liczba:
#             print("Liczba jest za duża. Spróbuj jeszcze raz.")
#
#         else:
#             print("Liczba jest za mała. Spróbuj jeszcze raz")
#
#         # Zwiększa liczbę prób
#         ile_prob += 1
#     print(f"Liczba prób: {ile_prob}")
#
# start = graj()
# print(start)
#
#
# # Zad_5
# # V_1
# def druga_najwieksza(lista):
#     # Usuwamy duplikaty, przekształcając listę w zestaw
#     unikalne_liczby = set(lista)
#
#     # Sprawdzamy, czy mamy co najmniej dwie różne liczby
#     if len(unikalne_liczby) < 2:
#         return None  # Jeśli lista nie zawiera co najmniej dwóch różnych liczb
#
#     # Sortujemy zestaw w porządku malejącym
#     unikalne_liczby = sorted(unikalne_liczby, reverse=True)
#
#     # Zwracamy drugą największą liczbę
#     return unikalne_liczby[1]
#
# # Przykładowa lista
# lista = [10, 20, 4, 45, 99, 99]
# wynik = druga_najwieksza(lista)
#
# print(f"Druga największa liczba w liście to: {wynik}")
#
# # V_2
# def druga_najwieksza(lista):
#     unikalne = list(set(lista))  # Usunięcie duplikatów
#     unikalne.sort(reverse=True)  # Sortowanie malejąco
#
#     if len(unikalne) < 2:
#         return "Brak drugiej największej wartości"  # Obsługa listy z 1 unikalnym elementem
#
#     return unikalne[1]  # Druga największa wartość
#
# lista = [10, 20, 4, 45, 99, 99]
# wynik = druga_najwieksza(lista)
# tab = list(range(0, 100, 5))
#
# print("Lista",lista)
# print(f"Druga największa liczba w liście to: {wynik}")
# print("Wygenerowane co 5 w zakresie 0-100: ",list(tab))
# print("Druga największa liczba w liście to:", druga_najwieksza(list(tab)))
# print("Druga największa liczba w liście to:", druga_najwieksza([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print("Druga największa liczba w liście to:", druga_najwieksza([19, 21, 22, 55, 19, 55, 33]))
# print("Druga największa liczba w liście to:", druga_najwieksza([99, 99]))
#
# # V_3
#
#
#
# # Zad_6
#
# import random
#
# # V_1
# def znajdz_min_max(macierz):
#     # Inicjalizacja zmiennych do przechowywania najmniejszej i największej wartości oraz ich indeksów
#     min_wartosc = float('inf')
#     max_wartosc = float('-inf')
#     min_indeks = (-1, -1)
#     max_indeks = (-1, -1)
#
# # Przechodzimy przez całą macierz, aby znaleźć min i max
#     for i in range(len(macierz)):
#         for j in range(len(macierz[i])):
#             # Sprawdzamy, czy obecna wartość jest najmniejsza
#             if macierz[i][j] < min_wartosc:
#                 min_wartosc = macierz[i][j]
#                 min_indeks = (i, j)
#             # Sprawdzamy, czy obecna wartość jest największa
#             if macierz[i][j] > max_wartosc:
#                 max_wartosc = macierz[i][j]
#                 max_indeks = (i, j)
#
#     # Wypisujemy oryginalną macierz z oznaczeniami "MIN" i "MAX"
#     for i in range(len(macierz)):
#         for j in range(len(macierz[i])):
#             if (i, j) == min_indeks:
#                 macierz[i][j] = "MIN"
#             elif (i, j) == max_indeks:
#                 macierz[i][j] = "MAX"
#
#     # Wypisanie zmodyfikowanej macierzy
#     for row in macierz:
#         print(row)
#
#     # Zwrócenie wartości MIN i MAX z ich indeksami
#     return min_wartosc, min_indeks, max_wartosc, max_indeks
#
# # Przykładowa macierz
# macierz = [[5, 2, 9, 8], [1, 7, 3, 4], [6, 0, 2, 5]]
#
# # Wywołanie funkcji
# min_wartosc, min_indeks, max_wartosc, max_indeks = znajdz_min_max(macierz)
#
# # Wypisanie wyników
# print(f"Najmniejsza wartość: {min_wartosc}, Indeks: {min_indeks}")
# print(f"Największa wartość: {max_wartosc}, Indeks: {max_indeks}")
#
# # V_2
# def znajdz_min_max(macierz):
#     # Inicjalizacja zmiennych do przechowywania najmniejszej i największej wartości oraz ich indeksów
#     min_wartosc = float('inf')
#     max_wartosc = float('-inf')
#     min_indeks = max_indeks = (-1, -1)
#
#     # Przechodzimy przez całą macierz, aby znaleźć min i max
#     for i, wiersz in enumerate(macierz):
#         for j, element in enumerate(wiersz):  # Iterowanie po elementach w wierszu
#             # Sprawdzamy, czy obecna wartość jest najmniejsza
#             if element < min_wartosc:
#                 min_wartosc = element
#                 min_indeks = (i, j)
#             # Sprawdzamy, czy obecna wartość jest największa
#             elif element > max_wartosc:
#                 max_wartosc = element
#                 max_indeks = (i, j)
#
#     # Wypisanie zmodyfikowanej macierzy
#     macierzy_wynik = [wiersz.copy() for wiersz in macierz]  # Tworzymy kopię macierzy
#     i_min, j_min = min_indeks
#     i_max, j_max = max_indeks  # Poprawnie przypisujemy indeksy do zmiennych
#
#     # Zmieniamy wartości min i max na 'MIN' i 'MAX'
#     macierzy_wynik[i_min][j_min] = 'MIN'
#     macierzy_wynik[i_max][j_max] = 'MAX'
#
#     return macierzy_wynik  # Zwracamy zmodyfikowaną macierz
#
#
# # Przykładowa macierz
# macierz = [[5, 2, 9, 8], [1, 7, 3, 4], [6, 0, 2, 5]]
#
# # Wywołanie funkcji i wypisanie wyników
# macierz_zmieniona = znajdz_min_max(macierz)
# for wiersz in macierz_zmieniona:
#     print(wiersz)

# # Zad_7
#
# Zmienna globalna do liczenia wywołań funkcji
# liczba_wywolania = -1
#
# def wynik(i):
#     global liczba_wywolania
#     liczba_wywolania += 1  # Zwiększamy licznik za każdym wywołaniem funkcji
#
#     if i < 5:
#         return 2  # Zmieniona wartość bazowa
#     elif i % 2 == 0:  # Jeśli i jest parzyste
#         return wynik(i-4) + wynik(i-2) + 2
#     else:  # Jeśli i jest nieparzyste
#         return wynik(i-2) % 9  # Zmieniona operacja mod
#
# # # Wczytanie wartości i od użytkownika
# # i = int(input("Podaj i: "))
#
# # # Wywołanie funkcji i wypisanie wyniku
# # print("Wynik:", wynik(i))
#
# # # Wypisanie liczby wywołań funkcji
# # print("Liczba wywołań funkcji:", liczba_wywolania)
#
# # Iterowanie po liczbach od 1 do 15
# for i in range(1, 16):
#     # Resetujemy licznik wywołań funkcji przed każdym nowym wywołaniem
#     liczba_wywolania = -1
#     wynik_dla_i = wynik(i)  # Wywołanie funkcji dla danej liczby i
#     print(f"Dla i = {i}: wynik = {wynik_dla_i}, liczba wywołań funkcji = {liczba_wywolania}")
#
# # # Zad_8
# def czy_palindrom(napis):
#     # Warunek bazowy: jeśli napis ma długość 0 lub 1, jest palindromem
#     if len(napis) <= 1:
#         return True
#     # Sprawdzamy, czy pierwszy i ostatni znak są takie same
#     elif napis[0] != napis[-1]:
#         return False
#     # Rekurencyjne wywołanie bez pierwszego i ostatniego znaku
#     return czy_palindrom(napis[1:-1])
#
# # Testy
# print(czy_palindrom("natan"))
# print(czy_palindrom("anna"))
# print(czy_palindrom("1221"))
# print(czy_palindrom("banan"))
# print(czy_palindrom("zakopanenapokaz"))
# print(czy_palindrom("zakopane na pokaz"))
# napis = input("Dowolny tekst: ")
# print(napis, "=", czy_palindrom(napis))

# V_2
def czy_palindrom(napis):
    # Warunek bazowy: jeśli napis ma długość 0 lub 1, jest palindromem
    if len(napis) <= 1:
        return True
    # Sprawdzamy, czy pierwszy i ostatni znak są takie same
    elif napis[0] != napis[-1]:
        return False
    # Rekurencyjne wywołanie bez pierwszego i ostatniego znaku
    return czy_palindrom(napis[1:-1])

# Pętla do ciągłego pobierania danych
while True:
    napis = input("Podaj tekst (lub wpisz 'q' / 'quit', lub 'E' / 'Exit', aby zakończyć): ").strip()
    if napis.lower() in ["q", "quit"] or napis.upper() in ["E", "Exit"]:  # Sprawdzenie warunku zakończenia
        print("Zakończono program.")
        break
    print(f"{napis} = {'jest palindromem' if czy_palindrom(napis) else 'nie jest palindromem'}")
