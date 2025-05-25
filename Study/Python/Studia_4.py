# x = 5
# if x > 2:
#     print("Większe niź 2")
#     print("Still bigger")
# print("Done with 2")
#
# for i in range(5):
#     print(i)
#     if i > 2:
#         print("Większe niź 2")
#     print("Koniec z ", i )
# print("Koniec kodu")
# print("______________________________________________________________________")
# x = 4
#
# if x > 2:
#     print("Biger")
# else:
#     print("Smaller")
# print("All done")
#
# print("______________________________________________________________________")
# x = 4
#
# if x < 2:
#     print("Small")
# elif x < 10:
#     print("Medium")
# else:
#     print("Large")
# print("All done")

# print("_____________________________FUNKCJE ( def, print, max_________________________________________")
#
# big = max("Hello word")
# print(big)
#
# print(type(big)) #sprawdzenie jakiego typu wartość jest
#
# tiny = min("Hello word")
# print(tiny)
#
# def greet(argument):
#     if argument == "es":
#         print("Hola")
#     elif argument == "fr":
#         print("Bonjour")
#     else:
#         print("Hello")
#
# greet("es")
# greet("fr")
# greet("pl")
#
#
# def greet():
#     return "Hello" #return kończy funkcę, pętle, i przekazuje parametr funkcji w miejsce argumentu
# print(greet(), "Paweł")
#
# def greet(argument):
#     if argument == "es":
#         return "Hola"
#     elif argument == "fr":
#         return "Bonjour"
#     else:
#         return "Witaj"
#
# print(greet("es"), "Paweł")
# print(greet("fr"), "Marcin")
# print(greet("pl"), "Wiesiek")
#
# def addtwo(a,b):
#     add = a + b
#     return add
# print("Wynik:", addtwo(3,5))
import random

# print("_____________________________Loops and Iteration_________________________________________")

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print("Well done")
# print(n)# ostatnią wartością w pętli dla n było 0 które nie było już brane ale zostało wpisane w parametr n

# while True:
#     line = input("Napisz co chcesz: ")
#     if line == "Done":
#         break
#     print(line)
# print("Will done")



# while True:
#     line = input("Napisz co chcesz: ")
#     if line[0] == "#": # nie wypisze tego znaku na konsoli
#         continue
#     elif line == "Done":
#         break
#
#     print(line)
#
# print("Will done")
#
# for i in [5,4,3,2,1]:
#     print(i)
#
#
# friends = ["Rysiek", "Wiesiek", "Paweł"]
#
# for i in friends:
#     print("Happy New Year", i)
# print("Done")
#
# #jak znaleźć największą liczbę
# larges_so_far = -1
# print("Before", larges_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if the_num > larges_so_far :
#         larges_so_far = the_num
#     print(larges_so_far, the_num)
# print("After", larges_so_far)
#
#
#
# # #jak znaleźć najmniejszą liczbę
# small_so_far = 100000 # można tak ale nie ma pewności jak jest pierwsza liczba
# print("Before", small_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if the_num < small_so_far :
#         small_so_far = the_num
#     print(small_so_far, the_num)
# print("After", small_so_far)
#
# # inny sposób
#
# smallest = None
# print("Before:", None)
# for value in [9,41,12,3,74,15]:
#     if smallest is None: # jeżeli smallest jest nieznana to podstaw pierwszą liczbę z listy czyli sprawdź na siebie, is jest używany do True lub Fase lub None, to nie to samo co ==
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print("After: ", smallest)




# # zlicza ile liczb jest na liście i je numeruje
# lp = 0
# print("Before", lp)
# for thing in [9,41,12,3,74,15]:
#     lp = lp + 1
#     print(lp, thing)
# print("After", lp)
#
# # dodaje do siebie kolejne liczby 9+0=9, 9+41=50, 50+12=62,

# lp = 0
# print("Before", lp)
# for thing in [9,41,12,3,74,15]:
#     lp = lp + thing
#     print(lp, thing)
# print("After", lp)

# # Wszystko razem zliczanie i suma z dodawania
# count = 0
# sum = 0
# print("Before", count, sum)
# for value in [9,41,12,3,74,15]:
#     count = count + 1
#     sum = sum + count
#     print(count, sum, value)
# print("After", count, sum, sum/count)
#
# # wypisanie najwyższej wartości z listy
#
# for value in [9,41,12,3,74,15]:
#     if value > 20 :
#         print("Liczby większe od 20:", value)
#
#
# # wyszukanie czy liczba 3 występuje w liście
# found = False
# print("Before: ", found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
#
# print("After: ", found)
#
# # inny sposób znajduje liczbę ale nie zmienia wartości dla innych liczb
#
# found = False
# print("Before: ", found)
# for value in [9,41,12,3,74,15]:
#     if value != 3:
#         print(found,value)
#
#     else:
#         found = True
#         print(True, value)
#
#
# print("After: ", found)

# # print("__________________________________Strings__________________________________")
#
# fruit = "banana" # liczy od 0 nie od 1
# letter = fruit[1]
# print(letter)
#
# x = 3
# w = fruit[x-1]
# print(w)
#
# print(len(fruit))# wyświetli 6 co jest nieprawdą liczy od 1, pamiętaj że dla len-1 jeśli chcesz zmienić wartość w str

# fruit = "banana"
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index,letter)
#     index = index + 1
#
# for letter in fruit:
#     print(letter)
#
# jak policzyć ilość wystąpień litery w stringu

# word = "banana"
# count = 0
# for letter in word:
#     if letter == "a":
#         count = count + 1
#
# print(letter,"=",count)
#
# s = "Monty Python"
#
# print(s[0:4])
# # Mont # od 0 up to not inclouding 4
#
# print(s[6:7])#spacja też jest traktowana jako znak
# # P
# print(s[6:20])#pozwoli na wykonanie i nie wyświetli że jest po za zakresem
# #  Python
# print(s[:2])
# # Mo
# print(s[6:])
# # Python
# print(s[:])
# # Monty Python
# # dodaj str nie zapomnij o spacji
# a = "hello"
# b = a + "world"
# print(b)
#
# c = a + " " + "world"
# print(c)
#
# fruit = "banana"
#
# if 'n' in fruit:
#     print("I'm found it")
#
# fruit = "banana"
# position = fruit.find("na")
# print(position)
# # 2
# greet = "Hello Word"
# zap = greet.lower()# zmienia w zminnej greet duże litery na małe i zapisuje w nowej zminnej zap
# print(zap)
# # inny sposób
# print(greet.lower())
# print("Cześć Paweł".lower())
# # cześć paweł
# print(dir(greet))# dir wyświetla wszystkie możliwości dla str greet
#
#
# greet = "Hello Word"
# print(greet.upper())
# #HELLO WORD
# print("cześć Paweł".upper())
# # CZEŚĆ PAWEŁ
#
# greet = "Hello Word"
# nstr = greet.replace("Word", "Pablo")
# print(nstr)
# # Hello Pablo
# nstr = greet.replace("l", "j")
# print(nstr)
# # Hejjo Word
#
# greet = "     Hello Word"
# print(greet)
# #      Hello Word
# print(greet.lstrip()) #przesuwa do początku w lewą stronę
# #Hello Word
# greet = "           Hello Word                "
# print(greet)
# print(greet.rstrip())# usuwa przerwe po prawej
# print(greet.strip())# usuwa po lewej i po prawej stronie str
#
# greet = "Hello Word"
#
# print(greet.startswith("H"))
# # True
# print(greet.startswith("h"))
# # False


# print("_________________________________DATA fom Outside____________________________")

# handle = open(filename, mode)
# return handle use to manipulate the filecmp
# filname is a string
# mode is a optional and shuld be "r" if we are planing to read the file and "w" if we are going to write to the file


# fhand = open('mbox.txt',"r")
# print(fhand)
# # _io.TextIOWraper name='mbox.tx' mode='r' encoding='UTF-8'

# stuff = "X\nY" # newline
# print(stuff)
# # X
# # Y
# print('\n')
# print(len(stuff))
# # 3

# import os
# print("Aktualny katalog roboczy:", os.getcwd())
# E:\Python_Project\test\venv\Scripts\python.exe E:/Python_Project/test/Studia_4.py
# Aktualny katalog roboczy: E:\Python_Project\test
#
# fhand = open("mbox.txt","r")
# for line in fhand:
#     print(line) # wyświetli wszystkie linie textu w dokumencie mbox.tx
#
# fhand = open("mbox.txt","r")
# count = 0
# for line in fhand:
#     count = count + 1
# print("Liczba lini:", count) #policzy linie tekstu
#
# fhand = open("mbox.txt","r")
# inp = fhand.read()
# print(len(inp))
# # 62
# print(inp[25:])
# # Bo che wiedziec czy dziala poprawnie
# # pdza60284@gmail.com
#
# fhand = open("mbox.txt","r")
# for line in fhand:
#     if line.startswith("pdz"): # drukuje linie która rozpoczyna się od pdz
#         print(line)
# print("\n")
# fhand = open("mbox.txt","r")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("pdz"): # drukuje linie która rozpoczyna się od pdz
#         print(line)
#
# print("\n")
# fhand = open("mbox.txt","r")
# for line in fhand:
#     line = line.rstrip()
#     if not "@gmail.com" in line: # drukuje linie w której zawiera się szukana fraza
#         continue
#     print(line)
#################################################################################
# fname = input("Enter the name:")
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith("pdz"):
#         count = count + 1
#     print("Ther wear" ,count, "pdz", fname)
#################################################################################
# fname = input("Enter the name:") # dodanie wyjątku jak nie znajdzie takiego pliku
# try:
#     fhand = open(fname)
# except:
#     print("File cannot be opened:", fname)
#     quit()
#
# count = 0
# for line in fhand:
#     if line.startswith("pdz"):
#         count = count + 1
#     print("Ther wear" ,count, "pdz", fname)
#
# print("____________________________________Dictionary,Listy,Data_____________________")
#
# ccc = dict()
# ccc["csev"] = 1 # for ccc[key] = value
# ccc['cwen'] = 1
# print(ccc)
# # {'csev': 1, 'cwen': 1} #po wyświetleniu słownika
# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc)
# # {'csev': 1, 'cwen': 2}
#
# print(ccc['cwen'])
# # 2
# print('csev' in ccc)
# # True
# ####################################################################

# lotto = [2, 14, 26,41,63]
# print(lotto)
# # [2, 14, 26, 41, 63]
# lotto[2] = 33
# print(lotto)
# # [2, 14, 33, 41, 63] # 0,1,2 - 26 zmieniamy na 33 tym samym zmieniamy zmienną lotto na stałe nie tak jak w str

# x = [1,2,'joe',99]
# print(len(x))
# # 4 # inaczej niż w str ti zlicza ile elementów jest w liście
##################################################################
# print(range(4))
# # range(0, 4)
# friends = ['John', 'Greg', 'Sally']
# print(len(friends))
# # 3
# print(list(range(len(friends))))
# # [0, 1, 2] # 0=John, 1=Greg, 3=Sally
#####################################################################################

# friends = ['John', 'Greg', 'Sally']
# for friend in friends:
#     print('Hapy NY: ', friend)
# # Hapy NY:  John
# # Hapy NY:  Greg
# # Hapy NY:  Sally
#
# for i in range(len(friends)):
#     friend = friends[i]
# print('Hapy NY', friend)
# # Hapy NY Sally
#####################################twożenie list##################

# stuff = list() # psta lista stuff
# stuff.append('book') # dodanie do listy zmiennych
# stuff.append(99)
# print(stuff)
# # ['book', '99']
# stuff.append('cookie')
# print(stuff)
# # ['book', 99, 'cookie']
#
# print(99 in  stuff)
# # True
# print(99 not in  stuff)
# # False

####################################sortowanie listy#######################

# friends = ['John', 'Greg', 'Sally']
# friends.sort()
# print(friends)
# # ['Greg', 'John', 'Sally']
# print(friends[1])
# # John

# numb = [1,4,5,77,8,11,17,92]
# print(max(numb))
# # 92
# print(min(numb))
# # 1
# print(sum(numb))
# # 215
# print(sum(numb)/len(numb))
# # 26.875 # Srednia

# numblist = list()
# while True:
#     inp = input('Enter number:')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numblist.append(value)
# average = sum(numblist)/len(numblist)
# print('Average (średnia): ',average)
# # Enter number:12
# # Enter number:2
# # Enter number:4
# # Enter number:12
# # Enter number:done
# # Average (średnia):  7.5



# counts = dict()
# names = ["csev",'cwen','csev','zqin','cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
#
# print(counts)
# # {'csev': 2, 'cwen': 2, 'zqin': 1}


# # get method for dictionaries
# if name in counts:
#     x = count[name]
# else:
#     x = 0
#
# x = counts.get(name, 0)
#

# counts = dict()
# names = ["csev",'cwen','csev','zqin','cwen']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1 # 0 to default, jeśli widzisz name to smo  1 +0 nastepny raz jak widzisz 1+1 itd
# print(counts)
# {'csev': 2, 'cwen': 2, 'zqin': 1}


#import numpy as np

# arr = np.array ([1,2,3],[4,5,6])
# print(arr)

# import random
#
# def genTab(n):
#     tab = []
#
#     for i in range(n):
#         tab.append(random.randrange(3, 10, 3))
#
#     return tab
#
# tablicaRandom = genTab(10)
# print(tablicaRandom)
#
#
# def szukajWielokrotnosci3(tab):
#     nowaTablica = []
#     for i in tab:
#         if i % 3 == 0:
#             nowaTablica.append(i)
#         elif i % 5 == 0:
#             nowaTablica.append(i)
#         elif i % 6 == 0:
#             nowaTablica.append(i)
#
#     return nowaTablica
#
# tablicaWielokrotnosci3 = szukajWielokrotnosci3(tablicaRandom)
# print(tablicaWielokrotnosci3)
#
#
# def polaczTablice(taba, tabb):
#     polaczaneTablice = taba + tabb
#
#     print(sum(polaczaneTablice))
#     print(min(polaczaneTablice))
#     print(max(polaczaneTablice))
#
#
# polaczTablice(tablicaRandom, tablicaWielokrotnosci3)
#

#
# def generujTablica(n):
#     tab = []
#     for i in range(n):
#         tab.append(random.randrange(3,30,3))
#     print("Tablica wypełniona n lasowymi liczbami z przedziału 3-30 z wielokrotnością 3:", tab)
#     tab2 = []
#     for j in tab:
#         if j % 3 == 0:
#             tab2.append(j)
#         elif j % 5 == 0:
#             tab2.append(j)
#         elif j % 6 == 0:
#             tab2a.append(j)
#     print("Nowa tablica z liczbami podzielnymi przez 3, 5, 6 to:", tab2)
#     return tab + tab2
#
#
# sumaTab = generujTablica(9)
# print("Połączone tablice", sumaTab)
#
#
# print("Minimalna liczba w tablicach:", min(sumaTab))
# print("Maksymalna wygenerowana wielokrotnośc liczby 3 w tablicach to:", max(sumaTab))

















