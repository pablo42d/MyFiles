
# # ______________________________________________________________________________________________________________
#
#
# # -------------------------------
# # Stos jako lista (bez limitu)
# # -------------------------------
#
# # Inicjalizacja stosu jako lista
# stos = []
#
# # Funkcja dodająca element na stos (PUSH -> DODAJ)
# def dodaj(stos, element):
#     stos.append(element)
#
# # Funkcja usuwająca element ze szczytu stosu (POP)
# def usun(stos):
#     if not czy_pusty(stos):
#         return stos.pop()
#     return "Stos jest pusty"
#
# # Funkcja zwracająca element na szczycie stosu (PEEK)
# def szczyt(stos):
#     if not czy_pusty(stos):
#         return stos[-1]
#     return "Stos jest pusty"
#
# # Funkcja sprawdzająca, czy stos jest pusty (IS_EMPTY)
# def czy_pusty(stos):
#     return len(stos) == 0
#
# # Funkcja wyświetlająca stos (od góry do dołu)
# def wyswietl_stos(stos):
#     print("Stos:", stos[::-1])
#
# # Przykład użycia
# dodaj(stos, 5)
# dodaj(stos, 10)
# dodaj(stos, 15)
# wyswietl_stos(stos)
# print("Szczyt:", szczyt(stos))       # Oczekiwane: 15
# print("Usunięto:", usun(stos))       # Oczekiwane: 15
# wyswietl_stos(stos)
#
# # -----------------------------------------
# # Stos z ograniczonym rozmiarem (dict)
# # -----------------------------------------
#
# # Inicjalizacja stosu z ograniczonym rozmiarem
# def inicjalizuj_stos(max_rozmiar):
#     return {"stos": [], "max_rozmiar": max_rozmiar}
#
# # Funkcja dodająca element na stos (PUSH)
# def dodaj(stos_dict, element):
#     if len(stos_dict["stos"]) < stos_dict["max_rozmiar"]:
#         stos_dict["stos"].append(element)
#     else:
#         print("Błąd: Stos osiągnął maksymalny rozmiar!")
#
# # Funkcja usuwająca element ze szczytu stosu (POP)
# def usun(stos_dict):
#     if not czy_pusty(stos_dict):
#         return stos_dict["stos"].pop()
#     return "Stos jest pusty"
#
# # Funkcja zwracająca element na szczycie stosu (PEEK)
# def szczyt(stos_dict):
#     if not czy_pusty(stos_dict):
#         return stos_dict["stos"][-1]
#     return "Stos jest pusty"
#
# # Funkcja sprawdzająca, czy stos jest pusty (IS_EMPTY)
# def czy_pusty(stos_dict):
#     return len(stos_dict["stos"]) == 0
#
# # Funkcja wyświetlająca stos (od góry do dołu)
# def wyswietl_stos(stos_dict):
#     print("Stos:", stos_dict["stos"][::-1])
#
# # Przykład użycia
# stos_bufor = inicjalizuj_stos(3)
# dodaj(stos_bufor, 5)
# dodaj(stos_bufor, 10)
# dodaj(stos_bufor, 15)
# dodaj(stos_bufor, 20)  # ❌ Błąd: Stos osiągnął maksymalny rozmiar!
# wyswietl_stos(stos_bufor)
# print("Pop:", usun(stos_bufor))
# wyswietl_stos(stos_bufor)
#
# # -----------------------------------------
# # Sortowanie stosu rekurencyjnie
# # -----------------------------------------
#
# def posortuj_stos(stos):
#     if len(stos) > 0:
#         ostatni = stos.pop()
#         posortuj_stos(stos)  # Sortowanie pozostałych elementów
#         wstaw_posortowany(stos, ostatni)
#
# def wstaw_posortowany(stos, element):
#     """Wstawia element do posortowanego stosu"""
#     if len(stos) == 0 or stos[-1] <= element:
#         stos.append(element)
#     else:
#         temp = stos.pop()
#         wstaw_posortowany(stos, element)
#         stos.append(temp)
#
# # Przykładowe użycie
# stos_do_sortowania = [30, 10, 50, 20, 40]
# posortuj_stos(stos_do_sortowania)
# print("Posortowany stos:", stos_do_sortowania)  # Oczekiwane: [10, 20, 30, 40, 50]


# ______________________________________________________________________________________________________________

# # 1. Napisz program, który wczyta ciąg liczb całkowitych od użytkownika, a następnie wyświetli je w odwrotnej kolejności, korzystając ze stosu.
#
# # Stos jako lista ver. A
# stos = []
#
# # Funkcja dodająca element na stos (PUSH)
# def dodaj(stos, element):
#     stos.append(element)
#
# # Funkcja wyświetlająca stos (od góry do dołu)
# def wyswietl_stos(stos):
#     print("Odwrócona kolejność:", stos[::-1])
#
# # Wczytywanie ciągu liczb od użytkownika
# wejscie = input("Wpisz liczby całkowite oddzielone spacją: ")
# liczby = [int(x) for x in wejscie.split()]
#
# # Dodawanie liczb na stos
# for liczba in liczby:
#     dodaj(stos, liczba)
#
# # Wyświetlenie liczb w odwrotnej kolejności
# wyswietl_stos(stos)
#
#
#
# # Stos jako lista ver.B
# stos = []
#
# # Funkcja dodająca element na stos
# def dodaj(stos, element):
#     stos.append(element)
#     # print("Stos", stos)
#
# # Funkcja wyświetlająca stos (od góry do dołu)
# def wyswietl_stos(stos):
#     print("Odwrócona kolejność:", stos[::-1])
#
# print("Wpisuj liczby całkowite. Wpisz 'q' aby zakończyć.")
#
# # Wczytywanie liczb po jednej
# while True:
#     wejscie = input("Podaj liczbę: ")
#     if wejscie.lower() == "q":
#         break
#     if wejscie.lstrip('-').isdigit():  # sprawdza, czy to liczba całkowita (obsługuje liczby ujemne)
#         dodaj(stos, int(wejscie))
#     else:
#         print("To nie jest liczba całkowita.")
#
# # Wyświetlenie liczb w odwrotnej kolejności
# print('Wprowadzono w kolejności:', stos)
# wyswietl_stos(stos)
#
#
#
# # 2. Napisz program wykorzystujący stos, który sprawdza, czy nawiasy w danym wyrażeniu są prawidłowo zagnieżdżone. Na przykład, wyrażenie "(()()(()))" jest prawidłowe, ale wyrażenia ")(" oraz "(()" są nieprawidłowe.
#
#
# # Funkcja sprawdzająca poprawność nawiasów
# def sprawdz_nawiasy(wyrazenie):
#     stos = []
#     for znak in wyrazenie:
#         if znak == '(':
#             stos.append(znak)
#         elif znak == ')':
#             if not stos:
#                 return False  # zamknięcie bez otwarcia
#             stos.pop()
#     return len(stos) == 0  # sprawdzenie, czy coś zostało na stosie
#
# # Przykładowe testy
# wyrazenia = [
#     "()",           # prawidłowe
#     ")(",           # nieprawidłowe
#     "(()",          # nieprawidłowe
# #     "",             # prawidłowe (brak nawiasów to też poprawne zagnieżdżenie)
#     "((())())()",   # prawidłowe
# #     "((())",        # nieprawidłowe
# ]
# # wyrazenia = [str(input("Wprowadż ciąg nawiasów: "))]
# for w in wyrazenia:
#     wynik = "PRAWIDŁOWE" if sprawdz_nawiasy(w) else "NIEPRAWIDŁOWE"
#     print("Wyrażenie: ", w, " - ", wynik)
#
#
# # 3. Napisz program, który symuluje mechanizm cofania ostatniej operacji (Undo). Program powinien pozwalać użytkownikowi dodawać teksty do stosu, a następnie cofać ostatnie operacje.
# # Zasady działania:
# # Użytkownik może dodać tekst - program zapisuje go na stosie.
# # Użytkownik może wykonać operację cofania (Undo) - program usuwa ostatni dodany tekst.
# # Program kończy działanie po wpisaniu "exit"
#
# # Stos do przechowywania operacji
# stos = []
#
# print("Wpisz tekst: ")
# print("Wpisz 'undo', aby cofnąć ostatnią operację.")
# print("Wpisz 'exit', aby zakończyć program.\n")
#
# while True:
#     wejscie = str(input("Wpisz polecenie: "))
#
#     if wejscie.lower() == "exit":
#         print("Zakończono program.")
#         break
#     elif wejscie.lower() == "undo":
#         if stos:
#             cofnij = stos.pop()
#             print(f"Cofnięto: '{cofnij}'")
#         else:
#             print("Brak operacji do cofnięcia.")
#     else:
#         stos.append(wejscie)
#         print(f"Dodano: '{wejscie}'")
#
#     print("Aktualna zawartość stosu:", " ".join(stos))
#
#
# # # 4. Napisz program, który wczytuje wyrażenie arytmetyczne zapisane w notacji postfiksowej (Odwrotna Notacja Polska) i oblicza jego wartość przy użyciu stosu.
# # # ONP (ang. RPN – Reverse Polish Notation) to metoda zapisu wyrażeń matematycznych, w której operatory są umieszczane po argumentach. Dzięki temu nie ma potrzeby stosowania nawiasów do określenia kolejności działań.
#
# def oblicz_onp(wyrazenie):
#  stos = []
#  operator = {"+", "-", "*", "/"}
#
#  for i in wyrazenie.split():
#   if i not in operator:
#    stos.append(float(i))  # dodaj liczbę na stos
#   else:
#    if len(stos) < 2:
#     return "Za mało argumentów do wykonania działania"
#    b = stos.pop()
#    a = stos.pop()
#
#    if i == "+":
#     stos.append(a + b)
#    elif i == "-":
#     stos.append(a - b)
#    elif i == "*":
#     stos.append(a * b)
#    elif i == "/":
#     if b == 0:
#      return "Dzielenie przez zero !!!"
#     stos.append(a / b)
#
#  if len(stos) != 1:
#   return "Niepoprawne wyrażenie"
#
#  return stos[0]
#
# # Przykładowe użycie
# wyrazenie = input("Podaj wyrażenie w ONP (np. '3 4 + 2 *'): ")
# wynik = oblicz_onp(wyrazenie)
# print(f"Wynik: {wynik}")
#
# # kolejki _____________________________________________________________________________________________
#
# # Importujemy moduł queue z biblioteki standardowej Pythona
# import queue
#
# # Tworzymy pustą kolejkę FIFO (First In, First Out)
# q = queue.Queue()
#
# # Dodajemy elementy do kolejki za pomocą metody put()
# q.put("zadanie1")  # Pierwsze zadanie
# q.put("zadanie2")  # Drugie zadanie
# q.put("zadanie3")  # Trzecie zadanie
#
# # Sprawdzamy liczbę elementów w kolejce
# print("Liczba zadań w kolejce:", q.qsize())
#
# # Sprawdzamy, czy kolejka jest pełna (dla maxsize = 0 zawsze False)
# print("Czy kolejka jest pełna?", q.full())
#
# # Pętla działa dopóki kolejka nie jest pusta
# while not q.empty():
#     # Pobieramy (i usuwamy) pierwszy element z kolejki
#     element = q.get()
#     # Wyświetlamy przetwarzany element
#     print("Przetwarzanie:", element)
#
# # Po wykonaniu wszystkich zadań
# print("Czy kolejka jest teraz pusta?", q.empty())
#
# # _________________________________________________________________________________________
#
# import queue  # Import standardowego modułu
#
# # Tworzymy kolejkę FIFO (First In, First Out)
# q = queue.Queue()
#
# # Sprawdzenie, czy kolejka jest pusta
# print("Czy kolejka pusta?", q.empty())  # True
#
# # Dodawanie elementów
# q.put(4)
# q.put("dog")
# q.put(True)
#
# # Sprawdzenie rozmiaru kolejki
# print("Liczba elementów:", q.qsize())  # 3
#
# # Sprawdzenie, czy kolejka jest pełna (tu brak limitu, więc zawsze False)
# print("Czy pełna?", q.full())  # False
#
# # Pobieranie elementów z kolejki (FIFO)
# print("Pobrano:", q.get())  # 4
# print("Pobrano:", q.get())  # "dog"
#
# # Ponowne sprawdzenie rozmiaru
# print("Liczba elementów po pobraniu:", q.qsize())  # 1
#
# # Usuwanie ostatniego elementu
# q.get()
#
# # Sprawdzenie, czy kolejka jest pusta po opróżnieniu
# print("Czy kolejka pusta po wszystkim?", q.empty())  # True
#
# # _____________________________________kolejka cykliczna (głowa, ogon)___________________________________
#
# class KolejkaCykliczna:
#  def __init__(self, rozmiar):
#   self.rozmiar = rozmiar
#   self.bufor = [None] * rozmiar
#   self.poczatek = 0
#   self.koniec = 0
#   self.licznik = 0
#
#  def enqueue(self, element):
#   if self.licznik == self.rozmiar:
#    print("Bufor pełny! Nie można dodać:", element)
#    return
#   self.bufor[self.koniec] = element
#   self.koniec = (self.koniec + 1) % self.rozmiar
#   self.licznik += 1
#
#  def dequeue(self):
#   if self.licznik == 0:
#    print("Bufor pusty! Nie można usunąć.")
#    return None
#   element = self.bufor[self.poczatek]
#   self.bufor[self.poczatek] = None  # opcjonalnie: czyścimy slot
#   self.poczatek = (self.poczatek + 1) % self.rozmiar
#   self.licznik -= 1
#   return element
#
#  def pokaz_bufor(self):
#   print("Bufor:", self.bufor)
#   print(f"Początek: {self.poczatek}, ➕ Koniec: {self.koniec}, Licznik: {self.licznik}")
#
#
# # Przykład użycia:
# kolejka = KolejkaCykliczna(5)
#
# kolejka.enqueue("A")
# kolejka.enqueue("B")
# kolejka.enqueue("C")
# kolejka.enqueue("D")
# kolejka.enqueue("E")
# kolejka.pokaz_bufor()
#
# # Próba dodania szóstego elementu
# kolejka.enqueue("F")  # powinno dać błąd
#
# # Usuwamy dwa elementy
# print("Usunięto:", kolejka.dequeue())
# print("Usunięto:", kolejka.dequeue())
# kolejka.pokaz_bufor()
#
# # Dodajemy nowe elementy, które „zawiną” się na początek bufora
# kolejka.enqueue("X")
# kolejka.enqueue("Y")
# kolejka.pokaz_bufor()
#
# # ------------------------------------------------------------------------------------------------------------
# # zad 5. Napisz program, który poprosi użytkownika o wpisanie 3 liczb. Każda z liczb ma zostać dodana do kolejki.
# # Po wpisaniu 3 liczb wyświetl poszczególne elementy kolejki.
#
# import queue
# q = queue.Queue()
#
# # Sprawdzenie, czy kolejka jest pusta
# print("Czy kolejka pusta?", q.empty())  # True
#
# # Dodawanie elementów
# for i in range(3):
#  n = int(input("Dodaj do kolejki: "))
#  q.put(n)
# # Sprawdzenie rozmiaru kolejki
# print("Liczba elementów:", q.qsize())  # 3
#
# while not q.empty():
#  print('Wyświetl kolejkę: ', q.get())
#
# # Sprawdzenie rozmiaru kolejki po wyprowadzeniu
# print("Liczba elementów:", q.qsize())  # 0

# # zad 6. Napisz funkcję, która zwróci w postaci listy n elementów kolejki. Jeżeli kolejka zawiera mniej niż n
# # elementów, funkcja ma zwrócić wszystkie dostępne elementy. Jeżeli kolejka jest pusta, funkcja ma zwrócić komunikat: „Kolejka jest pusta”.
#
# import queue
#
# # Tworzymy kolejkę FIFO
# q = queue.Queue()
#
# # Dodawanie elementów do kolejki
# for i in range(3):
#  l = int(input("Dodaj do kolejki: "))
#  q.put(l)
#
# # Pobierająca n elementów z kolejki q
# def pobierz_z_kolejki(q, n):
#  if q.empty():
#   return "Kolejka jest pusta"
#
#  lista = []
#  for _ in range(n):
#   if not q.empty():
#    lista.append(q.get()) # podgląda listę ale usuwa podglądane elementy
#   else:
#    break
#  return lista
#
# print("Wynik:", pobierz_z_kolejki(q, 2))
# print("Wynik:", pobierz_z_kolejki(q, 5))
# print(pobierz_z_kolejki(q, 1))  # Kolejka jest pusta
#
# #
# # def podejrzyj_elementy_z_kolejki(q, n):
# #  if q.empty():
# #   return "Kolejka jest pusta"
# #
# #  temp_q = queue.Queue()
# #  wynik = []
# #
# #  while not q.empty():
# #   element = q.get()
# #   if len(wynik) < n:
# #    wynik.append(element)
# #   temp_q.put(element)  # Zachowujemy element
# #
# #  # Przywracamy elementy do oryginalnej kolejki
# #  while not temp_q.empty():
# #   q.put(temp_q.get())
# #
# #  return wynik
# #
# # print("Podgląd:", podejrzyj_elementy_z_kolejki(q, 2))
# #
# # # Sprawdzamy, czy kolejka nadal zawiera wszystko:
# # while not q.empty():
# #     print("Z kolejki:", q.get())
# #
# # print("Podgląd po użyciu .get:", podejrzyj_elementy_z_kolejki(q, 5)) # Kolejka powinna być pusta
#
# # zad 7. kolejka w przychodni
#
# # class Kolejka:
# #  def __init__(self):
# #   self.kolejka = []
# #
# #  def enqueue(self, pacjent):
# #   self.kolejka.append(pacjent)
# #   print(f"Zarejestrowano pacjenta: {pacjent}")
# #
# #  def dequeue(self):
# #   if self.is_empty():
# #    print("Brak pacjentów w kolejce.")
# #   else:
# #    pacjent = self.kolejka.pop(0)
# #    print(f"Pacjent {pacjent} został wywołany do gabinetu.")
# #
# #  def is_empty(self):
# #   return len(self.kolejka) == 0
# #
# #  def show_queue(self):
# #   if self.is_empty():
# #    print("Kolejka jest pusta.")
# #   else:
# #    print("Aktualna kolejka pacjentów:")
# #    for i, pacjent in enumerate(self.kolejka, start=1):
# #     print(f"{i}. {pacjent}")
# #
# #
# # # Tworzymy instancję kolejki
# # przychodnia = Kolejka()
# #
# # # Menu główne
# # menu = '''\nWybierz działanie:
# # 1. Zarejestruj pacjenta
# # 2. Wywołaj pacjenta do gabinetu
# # 3. Pokaż aktualną kolejkę
# # 4. Zakończ działanie programu'''
# #
# # while True:
# #  print(menu)
# #  wybor = input("Twój wybór: ")
# #
# #  if wybor == "1":
# #   imie = input("Podaj imię pacjenta: ")
# #   przychodnia.enqueue(imie)
# #
# #  elif wybor == "2":
# #   przychodnia.dequeue()
# #
# #  elif wybor == "3":
# #   przychodnia.show_queue()
# #
# #  elif wybor == "4":
# #   print("👋 Zakończono działanie programu.")
# #   break
# #
# #  else:
# #   print("❗ Nieprawidłowy wybór. Wybierz 1–4.")
#
#
# class Kolejka:
#  def __init__(self):
#   self.kolejka = []
#   self.licznik = 1
#
#  def generuj_numer(self):
#   return f"P{self.licznik:03d}"
#
#  def enqueue(self):
#   numer = self.generuj_numer()
#   self.kolejka.append(numer)
#   print(f"Twój numer w kolejce to: {numer}")
#   self.licznik += 1
#
#  def dequeue(self):
#   if self.is_empty():
#    print("Brak pacjentów w kolejce.")
#   else:
#    numer = self.kolejka.pop(0)
#    print(f"Numer {numer} – proszę wejść do gabinetu.")
#
#  def is_empty(self):
#   return len(self.kolejka) == 0
#
#  def show_queue(self):
#   if self.is_empty():
#    print("Kolejka jest pusta.")
#   else:
#    print("Aktualna kolejka numerów:")
#    for i, numer in enumerate(self.kolejka, start=1):
#     print(f"{i}. {numer}")
#
#
# # Inicjalizacja kolejki
# przychodnia = Kolejka()
#
# # Menu
# menu = '''\n Wybierz działanie:
# 1. Zarejestruj pacjenta
# 2. Wywołaj pacjenta do gabinetu
# 3. Pokaż aktualną kolejkę
# 4. Zakończ działanie programu'''
#
# while True:
#  print(menu)
#  wybor = input("Twój wybór: ")
#
#  if wybor == "1":
#   przychodnia.enqueue()
#
#  elif wybor == "2":
#   przychodnia.dequeue()
#
#  elif wybor == "3":
#   przychodnia.show_queue()
#
#  elif wybor == "4":
#   print("Zakończono działanie programu.")
#   break
#
#  else:
#   print("Nieprawidłowy wybór. Wybierz 1–4.")
#
#
# # zad 8. Prorytet dla zadań w kolejce
#
# import heapq  # Importujemy moduł do obsługi kolejek priorytetowych
#
#
# class KolejkaZadan:
#  def __init__(self):
#   self.kolejka = []  # Lista do przechowywania zadań
#
#  # Dodawanie zadania do kolejki z priorytetem
#  def dodaj_zadanie(self, nazwa_zadania, priorytet):
#   heapq.heappush(self.kolejka, (priorytet, nazwa_zadania))
#   print(f"Dodano zadanie: '{nazwa_zadania}' z priorytetem {priorytet}")
#
#  # Obsługa zadania o najwyższym priorytecie (najniższa liczba)
#  def obsluz_zadanie(self):
#   if self.kolejka:
#    priorytet, zadanie = heapq.heappop(self.kolejka)
#    print(f"Obsługujemy zadanie: '{zadanie}' z priorytetem {priorytet}")
#   else:
#    print("Brak zadań w kolejce do obsługi.")
#
#  # Wyświetlanie wszystkich zadań w kolejce posortowanych według priorytetu
#  def pokaz_kolejke(self):
#   if self.kolejka:
#    print("Zadania w kolejce (posortowane według priorytetu):")
#    for priorytet, zadanie in self.kolejka:
#     print(f"Zadanie: '{zadanie}' z priorytetem {priorytet}")
#   else:
#    print("Brak zadań w kolejce.")
#
#
# def menu():
#  kolejka = KolejkaZadan()
#
#  while True:
#   # Wyświetlanie menu
#   print('''\nWybierz działanie:
# 1. Dodaj zadanie z priorytetem
# 2. Obsłuż zadanie o najwyższym priorytecie
# 3. Pokaż kolejkę zadań
# 4. Zakończ działanie programu''')
#
#   wybor = input("Wybierz opcję: ")
#
#   if wybor == '1':
#    nazwa_zadania = input("Podaj nazwę zadania: ")
#    priorytet = int(input("Podaj priorytet zadania (mniejsza liczba oznacza wyższy priorytet): "))
#    kolejka.dodaj_zadanie(nazwa_zadania, priorytet)
#
#   elif wybor == '2':
#    kolejka.obsluz_zadanie()
#
#   elif wybor == '3':
#    kolejka.pokaz_kolejke()
#
#   elif wybor == '4':
#    print("Zakończenie programu.")
#    break
#
#   else:
#    print("Nieprawidłowa opcja. Spróbuj ponownie.")
#
#
# # Uruchamiamy program
# menu()
#
#
# # zad 9. Kolejka w sklepie

class Klient:
 def __init__(self, imie, czas_obslugi):
  self.imie = imie
  self.czas_obslugi = czas_obslugi


class KolejkaSklepu:
 def __init__(self):
  self.kolejka = []

 def dodaj_klienta(self, imie, czas_obslugi):
  klient = Klient(imie, czas_obslugi)
  self.kolejka.append(klient)
  print(f"Dodano klienta {imie} z czasem obsługi {czas_obslugi} minut.")

 def obsluz_klienta(self):
  if self.kolejka:
   klient = self.kolejka.pop(0)
   print(f"Obsłużono klienta {klient.imie}. Czas obsługi: {klient.czas_obslugi} minut.")
  else:
   print("Brak klientów w kolejce.")

 def pokaz_kolejke(self):
  if not self.kolejka:
   print("Kolejka jest pusta.")
   return
  print("\nAktualna kolejka:")
  suma = 0
  for klient in self.kolejka:
   print(f"- {klient.imie}, czas oczekiwania: {suma} minut, obsługa: {klient.czas_obslugi} minut")
   suma += klient.czas_obslugi
  print()

 def menu(self):
  while True:
   print('''\nWybierz opcję:
1. Dodaj klienta do kolejki
2. Obsłuż klienta
3. Pokaż kolejkę z czasem oczekiwania
4. Zakończ program''')

   wybor = input("Twój wybór: ")

   if wybor == '1':
    imie = input("Podaj imię klienta: ")
    try:
     czas = int(input("Podaj szacowany czas obsługi (minuty): "))
     self.dodaj_klienta(imie, czas)
    except ValueError:
     print("Czas obsługi musi być liczbą całkowitą.")
   elif wybor == '2':
    self.obsluz_klienta()
   elif wybor == '3':
    self.pokaz_kolejke()
   elif wybor == '4':
    print("Zakończono program.")
    break
   else:
    print("Nieprawidłowy wybór. Spróbuj ponownie.")


# Uruchomienie programu
kolejka = KolejkaSklepu()
kolejka.menu()
