# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#
# # Wczytaj liczbę graczy
# n = int(input("Podaj liczbę graczy: "))
#
# # Wczytaj wyniki graczy
# wyniki = []
# for i in range(n):
#     wynik = int(input(f"Podaj wynik gracza {i + 1}: "))
#     wyniki.append(wynik)
#
# # Posortuj wyniki za pomocą sortowania bąbelkowego
# bubble_sort(wyniki)
#
# # Wyświetl posortowaną listę wyników
# print("\nPosortowane wyniki:")
# print(wyniki)
#
# # Wyświetl najniższy i najwyższy wynik
# print(f"Najniższy wynik: {wyniki[0]}")
# print(f"Najwyższy wynik: {wyniki[-1]}")
#
# # Zad_3
def merge_sort(l, r, A, B, poziom=0):
    if r - l < 1:
        return

    m = (l + r + 1) // 2

    # Sortujemy lewą część
    merge_sort(l, m - 1, A, B, poziom + 1)

    # Sortujemy prawą część
    merge_sort(m, r, A, B, poziom + 1)

    # Wypisujemy szczegóły przed scaleniem
    print(f"{'  '*poziom}Scalanie: l={l}, m={m}, r={r}")
    print(f"{'  '*poziom}  Lewa  = {A[l:m]}")
    print(f"{'  '*poziom}  Prawa = {A[m:r+1]}")

    merge(l, m, r, A, B)

    # Wypisujemy wynik po scaleniu
    print(f"{'  '*poziom}  Po scaleniu: {A[l:r+1]}")


def merge(l, m, r, A, B):
    i = l
    j = m
    k = l

    while i < m and j <= r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i < m:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= r:
        B[k] = A[j]
        j += 1
        k += 1

    for t in range(l, r + 1):
        A[t] = B[t]


# Przykład użycia:
A = [63, 7, 29, 45, 3, 81, 18, 2, 54, 19]
B = [0] * len(A)

print("Startowa tablica:", A)
merge_sort(0, len(A) - 1, A, B)
print("Posortowana tablica:", A)


#---------------------------------------------------inny kod -----------------------
# data = [63, 7, 29, 45, 3, 81, 18, 2, 54, 19]
#
# merge_steps = []
# index_steps = []
#
#
# def merge_sort(arr, l, r, level=1):
#     if l < r:
#         m = (l + r) // 2
#         # Zapisujemy indeksy l, m, r i poziom
#         index_steps.append((level, l, m, r))
#
#         # Sortowanie lewej i prawej części
#         merge_sort(arr, l, m, level + 1)
#         merge_sort(arr, m + 1, r, level + 1)
#
#         # Scalanie i zapisywanie kroków
#         merge(arr, l, m, r, level)
#
#
# def merge(arr, l, m, r, level):
#     left = arr[l:m + 1]
#     right = arr[m + 1:r + 1]
#     i = j = 0
#     k = l
#
#     original = arr[:]
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1
#
#     # Zapisujemy krok scalania
#     merge_steps.append({
#         'level': level,
#         'left': left,
#         'right': right,
#         'merged': arr[l:r + 1]
#     })
#
#
# # Uruchomienie sortowania
# merge_sort(data, 0, len(data) - 1)
#
# # Wyświetlenie wyników
# print("Kroki scalania:")
# for step in merge_steps:
#     print(f"Poziom {step['level']}: Lewa: {step['left']}, Prawa: {step['right']}, Po scaleniu: {step['merged']}")
#
# print("\nIndeksy l, m, r dla każdego etapu:")
# for level, l, m, r in index_steps:
#     print(f"Poziom {level}: l = {l}, m = {m}, r = {r}")
#
# print("\nWynik końcowy:", data)
#
# -----------------------------------------------------------------------------------------------------
#
# # Zadanie 4 insertion_sort
#
# def insertion_sort(tablica):
#     print("Początkowa tablica:", tablica)
#     for i in range(1, len(tablica)):
#         element = tablica[i]
#         j = i - 1
#         print(f"\n--- Krok i={i}, element={element} ---")
#         while j >= 0 and tablica[j] > element:
#             print(f"A[{j}] = {tablica[j]} > {element} → przesuwam A[{j}] na pozycję {j+1}")
#             tablica[j + 1] = tablica[j]
#             j -= 1
#         tablica[j + 1] = element
#         print("Stan tablicy po wstawieniu:", tablica)
#
#     print("\nTablica po sortowaniu:", tablica)
#
# # Przykładowe dane
# a = [3, 5, 2, 6, 4, 1]
# insertion_sort(a)
#
#

# # Zad_5 algorytm Selection Sort
#
# def selection_sort(wagi):
#     n = len(wagi)
#     liczba_porownan = 0
#
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             liczba_porownan += 1
#             if wagi[j] < wagi[min_index]:
#                 min_index = j
#
#         # Zamiana elementów
#         wagi[i], wagi[min_index] = wagi[min_index], wagi[i]
#
#         # Wyświetlenie listy po każdej iteracji
#         print(f"Iteracja {i + 1}: {wagi}")
#
#     print(f"\nŁączna liczba porównań: {liczba_porownan}")
#
# # Dane wejściowe
# wagi_paczek = [18, 5, 12, 3, 9]
#
# # Wywołanie funkcji
# selection_sort(wagi_paczek)
#
#
# # Zad_6 wyszukiwanie_liniowe
#
# def wyszukiwanie_liniowe(lista, szukana_wartosc):
#     for i in range(len(lista)):
#         if lista[i] == szukana_wartosc:
#             return i  # Zwróć indeks pierwszego wystąpienia
#     return -1  # Zwróć -1, jeśli nie znaleziono
#
# # Przykłady użycia:
# print(wyszukiwanie_liniowe([4, 7, 2, 9, 5], 9))   # Output: 3
# print(wyszukiwanie_liniowe([10, 20, 30, 40], 25)) # Output: -1
#
# # Zad_7 wyszukiwanie_interpolacyjne
#
# def wyszukiwanie_interpolacyjne(lista, szukana):
#     start = 0
#     end = len(lista) - 1
#     krok = 1
#
#     while start <= end and szukana >= lista[start] and szukana <= lista[end]:
#         # Zapobiegamy dzieleniu przez zero
#         if lista[start] == lista[end]:
#             if lista[start] == szukana:
#                 print(f"Krok {krok}: start = {start}, end = {end}, mid = {start}, lista[mid] = {lista[start]}")
#                 return start
#             else:
#                 break
#
#         # Oblicz mid według wzoru interpolacyjnego
#         mid = start + ((szukana - lista[start]) * (end - start)) // (lista[end] - lista[start])
#
#         print(f"Krok {krok}: start = {start}, end = {end}, mid = {mid}, lista[mid] = {lista[mid]}")
#
#         if lista[mid] == szukana:
#             return mid
#         elif lista[mid] < szukana:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#         krok += 1
#
#     return -1
#
# # Przykład użycia:
# lista = [12, 18, 24, 30, 36, 42, 48, 54, 60]
# szukana = 36
# wynik = wyszukiwanie_interpolacyjne(lista, szukana)
#
# if wynik != -1:
#     print(f"\nWartość {szukana} znaleziona na pozycji {wynik}.")
# else:
#     print(f"\nWartość {szukana} nie została znaleziona.")
#
#
# # Zad_8 quick_select
#
# import random
#
# def quick_select(tablica, k):
#     if len(tablica) == 1:
#         return tablica[0]
#
#     pivot = random.choice(tablica)
#     mniejsze = [x for x in tablica if x < pivot]
#     rowne = [x for x in tablica if x == pivot]
#     wieksze = [x for x in tablica if x > pivot]
#
#     if k <= len(mniejsze):
#         return quick_select(mniejsze, k)
#     elif k <= len(mniejsze) + len(rowne):
#         return pivot
#     else:
#         return quick_select(wieksze, k - len(mniejsze) - len(rowne))
#
# # Przykład:
# tablica = [12, 3, 5, 7, 4, 19, 26]
# k = 3
# print(f"{k}-ty najmniejszy element to: {quick_select(tablica, k)}")
#
# # Zad_9 rabin_karp
#
# def rabin_karp(text, pattern, mod=101):
#     pattern_len = len(pattern)
#     pattern_hash = sum(ord(c) for c in pattern) % mod
#     print(f"Hash wzorca '{pattern}': {pattern_hash}\n")
#
#     matches = []
#
#     print(f"{'Fragment':<8} {'Pozycja':<8} {'Suma ASCII':<12} {'Hash':<6} Komentarz")
#     print("-" * 60)
#
#     for i in range(len(text) - pattern_len + 1):
#         fragment = text[i:i+pattern_len]
#         fragment_sum = sum(ord(c) for c in fragment)
#         fragment_hash = fragment_sum % mod
#
#         komentarz = "brak dopasowania"
#         if fragment_hash == pattern_hash:
#             if fragment == pattern:
#                 komentarz = "dopasowanie, znaki OK"
#                 matches.append(i)
#             else:
#                 komentarz = "hash zgodny, znaki różne"
#
#         print(f"{fragment:<8} {i:<8} {fragment_sum:<12} {fragment_hash:<6} {komentarz}")
#
#     print("\nPozycje dopasowań:", matches)
#
# # Dane wejściowe
# text = "thesunrisesatsunset"
# pattern = "sun"
#
# # Uruchomienie
# rabin_karp(text, pattern)
