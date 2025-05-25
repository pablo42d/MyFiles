# # zad_1
#
# n = 5
#
# for i in range(n):
#     print ("iteracja dla pętli właściwej i:", i+1,"z",n)
#     for j in range(n//2):
#         print("iteracja pętli wewnętrznej dla j", j+1,"z",n//2)
# print ("to jest liczba i wykonanych powtórzeń dla pętli zewnętrznej",i+1,", ilośc wykonanych operacji w pętli wewnętrznej",(j+1)*n,", łączna ilośc operacji wykonywanych to ",(n)+((1+j)*n))
# print ("Big-O(n) = ",n**2)

# # zad_2
#
# n = int(input("Podaj liczbę n: "))
#
# sum = 0
# for i in range(n):
#     print(i+1,"z",n)
#     # k=0
#     for j in range(2 * n):  #wykona się 2 razy n dla kazdego i z pętli nadrzędnej
#         sum += i + j
#         # k += i + j
#         # print(k)
#         print("dla i=",i, "dla j=",j,"suma iteracji i+j=",i+j,"ile iteracji w pętli zagnieżdżonej",j+1,"z",2*n)
#     print("Suma i+j+ wynik z każdego powtórenia z pętli i:",sum,"ile powtórzeń dla pętli i:",i+1,"ile powtórzeń dla pętli wewnętrznej j:",j+1)
#
# # zad_3
#
# # zad_4
#
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     steps = 0  # Licznik kroków
#
#     while left <= right:
#         steps += 1
#         mid = (left + right) // 2  # Obliczenie środkowego indeksu
#
#         print(f"Krok {steps}: Sprawdzam indeks {mid}, wartość {arr[mid]}")
#
#         if arr[mid] == target:
#             print(f"Znaleziono {target} na indeksie {mid} po {steps} krokach.")
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1  # Szukamy w prawej części tablicy
#         else:
#             right = mid - 1  # Szukamy w lewej części tablicy
#
#     print(f"Nie znaleziono {target} po {steps} krokach.")
#     return -1  # Zwracamy -1, jeśli elementu nie ma w tablicy
#
# # Dane wejściowe
# arr = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
# target = 55
#
# # Uruchomienie algorytmu
# binary_search(arr, target)


# Zad_4 inne

# def binary_search_recursive(arr, left, right, target):
#     if left > right:
#         return -1  # Element nie został znaleziony
#
#     mid = left + (right - left) // 2  # Obliczenie środkowego indeksu
#
#     if arr[mid] == target:
#         return mid  # Znaleziono element
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, mid + 1, right, target)  # Przeszukiwanie prawej połowy
#     else:
#         return binary_search_recursive(arr, left, mid - 1, target)  # Przeszukiwanie lewej połowy
#
#
# # Przykładowa posortowana tablica
# tablica = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
# cel = 55  # Szukana wartość
#
# # Wywołanie funkcji
# wynik = binary_search_recursive(tablica, 0, len(tablica) - 1, cel)
#
# # Wyświetlenie wyniku
# if wynik != -1:
#     print(f"Element {cel} znaleziony na indeksie {wynik}.")
# else:
#     print("Element nie znajduje się w tablicy.")
#
#
# # Zad_5
# # iteracyjną implementację wyszukiwania binarnego O(log n)(lepsza pod pamięć)
# def binary_search_iterative(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = left + (right - left) // 2
#
#         if arr[mid] == target:
#             return mid  # Znaleziono element
#         elif arr[mid] < target:
#             left = mid + 1  # Przeszukiwanie prawej połowy
#         else:
#             right = mid - 1  # Przeszukiwanie lewej połowy
#
#     return -1  # Element nie został znaleziony
#
#
# # Przykładowa posortowana tablica
# tablica = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
# cel = 55  # Szukana wartość
#
# # Wywołanie funkcji
# wynik = binary_search_iterative(tablica, cel)
#
# # Wyświetlenie wyniku
# if wynik != -1:
#     print(f"Element {cel} znaleziony na indeksie {wynik}.")
# else:
#     print("Element nie znajduje się w tablicy.")
#
#
# # rekurencyjne implementacja wyszukiwania binarnego O(log n) (gorsza pod względem pamięci)
#
def wyszukiwanie_binarne(tab, szukana_wartosc, lewy, prawy):
     # Znajdujemy środkowy element
    srodkowy = (lewy + prawy) // 2

    # Sprawdzamy, czy środkowy element to ten, którego szukamy
    if tab[srodkowy] == szukana_wartosc:
        return srodkowy  # Zwracamy indeks środkowego elementu

    # Jeśli szukana wartość jest mniejsza od środkowego elementu
    elif tab[srodkowy] > szukana_wartosc:
        return wyszukiwanie_binarne(tab, szukana_wartosc, lewy, srodkowy - 1)
    # Jeśli szukana wartość jest większa od środkowego elementu
    else:
        return wyszukiwanie_binarne(tab, szukana_wartosc, srodkowy + 1, prawy)

tab = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
szukana_wartosc = 7

wynik = wyszukiwanie_binarne(tab, szukana_wartosc, 0, len(tab) - 1)
print(tab)
print(szukana_wartosc,'znajduje się na indeksie:',wynik)
# if wynik != -1:
#     print(f"Znaleziono {szukana_wartosc} na indeksie {wynik}")
# else:
#     print(f"Nie znaleziono {szukana_wartosc}")


# # Zad_6 problem plecakowy rekurencja z memonizacją
#
# def plecak_rekurencyjny(liczba_przedmiotow, pojemnosc, wartosci, wagi, memo):
#     # Sprawdzamy, czy wynik dla tego podproblemu został już zapisany w pamięci memo
#     if (liczba_przedmiotow, pojemnosc) in memo:
#         return memo[(liczba_przedmiotow, pojemnosc)]
#
#     # Jeśli nie ma przedmiotów lub pojemność plecaka wynosi 0, zwracamy 0
#     if liczba_przedmiotow == 0 or pojemnosc == 0:
#         return 0
#
#     # Jeśli przedmiot nie mieści się w plecaku o pojemności C
#     if wagi[liczba_przedmiotow - 1] > pojemnosc:
#         wynik = plecak_rekurencyjny(liczba_przedmiotow - 1, pojemnosc, wartosci, wagi, memo)
#     else:
#         # Sprawdzamy, czy lepiej nie wziąć przedmiotu lub go wziąć
#         wynik = max(
#             plecak_rekurencyjny(liczba_przedmiotow - 1, pojemnosc, wartosci, wagi, memo),
#             wartosci[liczba_przedmiotow - 1] + plecak_rekurencyjny(liczba_przedmiotow - 1, pojemnosc - wagi[liczba_przedmiotow - 1], wartosci, wagi, memo)
#         )
#
#     # Zapamiętujemy wynik dla tego podproblemu
#     memo[(liczba_przedmiotow, pojemnosc)] = wynik
#     return wynik
#
# # Funkcja pomocnicza do wywołania rekurencyjnego (algorytmu z memonizacją)
# def plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi):
#     memo = {}  # Słownik do zapisywania wyników podproblemów
#     return plecak_rekurencyjny(liczba_przedmiotow, pojemnosc, wartosci, wagi, memo)
#
# # Testowanie funkcji
# liczba_przedmiotow = 4  # Liczba dostępnych przedmiotów
# pojemnosc = 7  # Maksymalna pojemność plecaka
# wartosci = [1, 4, 5, 7]  # Wartości przedmiotów
# wagi = [1, 3, 4, 5]  # Wagi przedmiotów
#
# # Wywołanie funkcji i wyświetlenie wyniku
# wynik = plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi)
# print("Maksymalna wartość, jaką można uzyskać:", wynik)

# # Podaje jaki index wartość i waga były wybrane
#
# def plecak_rekurencyjny(liczba_przedmiotow, pojemnosc, wartosci, wagi, memo):
#     # Sprawdzamy, czy wynik dla tego podproblemu został już zapisany w pamięci memo
#     if (liczba_przedmiotow, pojemnosc) in memo:
#         return memo[(liczba_przedmiotow, pojemnosc)]
#
#     # Jeśli nie ma przedmiotów lub pojemność plecaka wynosi 0, zwracamy 0 i pustą listę
#     if liczba_przedmiotow == 0 or pojemnosc == 0:
#         return 0, []
#
#     # Jeśli przedmiot nie mieści się w plecaku, pomijamy go
#     if wagi[liczba_przedmiotow - 1] > pojemnosc:
#         wynik = plecak_rekurencyjny(liczba_przedmiotow - 1, pojemnosc, wartosci, wagi, memo)
#     else:
#         # Opcja 1: Nie bierzemy przedmiotu
#         wartosc_bez, przedmioty_bez = plecak_rekurencyjny(liczba_przedmiotow - 1, pojemnosc, wartosci, wagi, memo)
#
#         # Opcja 2: Bierzemy przedmiot
#         wartosc_z, przedmioty_z = plecak_rekurencyjny(liczba_przedmiotow - 1, pojemnosc - wagi[liczba_przedmiotow - 1], wartosci, wagi, memo)
#         wartosc_z += wartosci[liczba_przedmiotow - 1]
#
#         # Wybieramy lepszą opcję
#         if wartosc_z > wartosc_bez:
#             wynik = (wartosc_z, przedmioty_z + [(liczba_przedmiotow - 1, wartosci[liczba_przedmiotow - 1], wagi[liczba_przedmiotow - 1])])
#         else:
#             wynik = (wartosc_bez, przedmioty_bez)
#
#     # Zapamiętujemy wynik w memo
#     memo[(liczba_przedmiotow, pojemnosc)] = wynik
#     return wynik
#
#
# # Funkcja pomocnicza do wywołania rekurencyjnego (algorytmu z memoizacją)
# def plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi):
#     memo = {}  # Słownik do zapisywania wyników podproblemów
#     return plecak_rekurencyjny(liczba_przedmiotow, pojemnosc, wartosci, wagi, memo)
#
#
# # Testowanie funkcji
# liczba_przedmiotow = 4  # Liczba dostępnych przedmiotów
# pojemnosc = 7  # Maksymalna pojemność plecaka
# wartosci = [1, 4, 5, 7]  # Wartości przedmiotów
# wagi = [1, 3, 4, 5]  # Wagi przedmiotów
#
# # Wywołanie funkcji i wyświetlenie wyniku
# maks_wartosc, wybrane_przedmioty = plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi)
#
# print("Wybrane przedmioty (indeks, wartość, waga):", wybrane_przedmioty)
# print("Maksymalna wartość, jaką można uzyskać:", maks_wartosc)
#
#


# inna rekurencja bez memonizacji gorsza
#
# def plecak_rekurencyjny(n, pojemnosc, wartosci, wagi):
#     # Przypadek bazowy: jeśli nie ma przedmiotów lub pojemność plecaka wynosi 0
#     if n == 0 or pojemnosc == 0:
#         return 0
#
#     # Jeśli waga n-tego przedmiotu jest większa niż aktualna pojemność plecaka, pomijamy go
#     if wagi[n - 1] > pojemnosc:
#         return plecak_rekurencyjny(n - 1, pojemnosc, wartosci, wagi)
#
#     # Sprawdzamy maksymalną wartość z dwóch możliwości:
#     # 1. Pomijamy n-ty przedmiot
#     # 2. Dodajemy n-ty przedmiot i odejmujemy jego wagę od pojemności
#     return max(
#         plecak_rekurencyjny(n - 1, pojemnosc, wartosci, wagi),
#         wartosci[n - 1] + plecak_rekurencyjny(n - 1, pojemnosc - wagi[n - 1], wartosci, wagi)
#     )
#
#
# # Testowanie funkcji
# liczba_przedmiotow = 4  # Liczba dostępnych przedmiotów
# pojemnosc = 7  # Maksymalna pojemność plecaka
# wartosci = [1, 4, 5, 7]  # Wartości przedmiotów
# wagi = [1, 3, 4, 5]  # Wagi przedmiotów
#
# # Wywołanie funkcji i wyświetlenie wyniku
# print("Maksymalna wartość, jaką można uzyskać:", plecak_rekurencyjny(liczba_przedmiotow, pojemnosc, wartosci, wagi))

# wersja iteracyjna
#
# def plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi):
#      # Tworzymy tablicę dp, gdzie dp[i][j] oznacza maksymalną wartość możliwą
#      # do uzyskania przy użyciu pierwszych i przedmiotów i plecaka o pojemności j.
#      dp = [[0] * (pojemnosc + 1) for _ in range(liczba_przedmiotow + 1)]
#      # Iteracja przez przedmioty
#      for i in range(1, liczba_przedmiotow + 1):
#          # Iteracja przez możliwe pojemności plecaka
#          for j in range(pojemnosc + 1):
#              # Jeśli przedmiot i-ty nie mieści się w plecaku o pojemności j,
#              # to przepisujemy wartość z wiersza powyżej (nie bierzemy go)
#              if wagi[i - 1] > j:
#                  dp[i][j] = dp[i - 1][j]
#              else:
#                  # Możemy albo pominąć przedmiot (dp[i-1][j]),
#                  # albo dodać go do plecaka i sprawdzić, czy suma wartości jest większa
#                  dp[i][j] = max(dp[i - 1][j], wartosci[i - 1] + dp[i - 1][j - wagi[i - 1]])
#                  # Zwracamy największą możliwą wartość dla wszystkich przedmiotów i pełnej pojemności plecaka
#      return dp[liczba_przedmiotow][pojemnosc]
# # Testowanie funkcji
# liczba_przedmiotow = 4  # Liczba dostępnych przedmiotów
# pojemnosc = 7  # Maksymalna pojemność plecaka
# wartosci = [1, 4, 5, 7]  # Wartości przedmiotów
# wagi = [1, 3, 4, 5]  # Wagi przedmiotów
# # Wywołanie funkcji i wyświetlenie wyniku
# print("Maksymalna wartość, jaką można uzyskać:", plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi))

#
# print(-----------------------------------------------------------------------------)
#
# def selection_sort(arr):
#     n = len(arr)
#     print("Elementów w liście:",n-1)    #len przypisuje indeksy 1,2,3,4.... wiec musimy zmnieszyć ilość o 1
#     for i in range(n - 1):  # Przechodzimy przez całą listę
#         min_idx = i  # Zakładamy, że pierwszy element w tej iteracji jest najmniejszy
#         print("pierwszy najmniejszy element", min_idx, '=',arr[min_idx])
#         for j in range(i + 1, n):  # Szukamy najmniejszego elementu w pozostałej części listy
#             if arr[j] < arr[min_idx]:
#                 print(arr[j], "<", arr[min_idx])
#                 min_idx = j  # Znaleźliśmy nowy najmniejszy element
#                 print("Nowy najmniejszy element o indeksie:", min_idx, '= jest wartości', arr[min_idx])
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Zamiana miejscami
#         print(arr[i], arr[min_idx], '=', arr[min_idx], arr[i])
#     return arr
#
# # Przykład użycia:
# arr = [7, 6, 1, 9, 5]
# print('Lista do sortowania przez wstawianie', arr)
# print("Sortowanie przez wstawianie", selection_sort(arr))  # Output: [1, 5, 6, 7, 9]



# def insertion_sort(arr):
#     for i in range(1, len(arr)):  # Zaczynamy od drugiego elementu
#         print('index', i)
#         key = arr[i]
#         print("wartość", key)
#         j = i - 1
#         print("index j", j)
#         while j >= 0 and arr[j] > key:  # Przesuwanie większych elementów
#             arr[j + 1] = arr[j]
#             print(arr)
#             print(arr[j + 1], arr[j])
#             j -= 1
#             print("index j", j)
#         arr[j + 1] = key  # Wstawienie elementu w odpowiednie miejsce
#         print("arr na miejsce", arr)
#     return arr
#
# # Przykład użycia:
# arr = [5, 3, 8, 4, 2]
# print('Lista do sortowania przez wybieranie', arr)
# print("Posortowana lista:", insertion_sort(arr))  # Output: [2, 3, 4, 5, 8]
#
#
#

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(n - 1 - i):  # Przechodzimy przez listę, ignorując już posortowaną część
#             if arr[j] > arr[j + 1]:  # Zamiana miejscami, jeśli elementy są w złej kolejności
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:  # Jeśli w tej iteracji nie było zamian, to lista jest już posortowana
#             break
#     return arr
#
# # Przykład użycia:
# arr = [5, 3, 8, 4, 2]
# print(bubble_sort(arr))  # Output: [2, 3, 4, 5, 8]
