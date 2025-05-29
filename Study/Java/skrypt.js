// asynk - kto pierwszy ten lepszy 
// <script src="../Java/skrypt.js" async></script>
// uruchomienie skryptu w kolejności w jakiej został wstawiony do dokumentu
// <script src="../Java/skrypt.js" defer></script> 

console.log("Witaj w debugerze - zobaczysz ten kod w konsoli przeglądarki po F12")
console.error("To jest Błąd - na czerwono")
console.warn("To jest ostrzerzenie - na żółto")


// zapis dla starych przeglądarek:--coś nie działa do końca poprawnie
// {/* <script>
// <!--

// Okna dialogowe

var zmienna="Java Script";
alert("Witaj w "+zmienna);
confirm("Czy chcesz kontynuować?") ? console.log("Użytkownik wybrał OK") : console.log("Użytkownik wybrał Anuluj");
// lub inny sposób
if(confirm("Czy chcesz kontynuować?")) {
    alert("Użytkownik wybrał OK");
} else {"Użytkownik wybrał Anuluj";
}

var imię = prompt("Podaj swoje imię:");
if (imię) {
    console.log("Użytkownik podał imię" + imię);
    alert("Witaj " + imię);
} else {
    console.log("Użytkownik nie podał imienia");
    alert("Witaj nieznajomy");
}


// document.write("To jest napis w dokumencie HTML");
// document.getElementById("wynik").innerHTML = "To jest napis w elemencie HTML o id 'wynik'";
// console.log("To jest napis w konsoli przeglądarki");


// Wstawianie tekstu do dokumentu HTML
function wstawTekst() {
    // document.write("To jest napis w dokumencie HTML");
    document.getElementById("wynik").innerHTML = "To jest napis w elemencie HTML o id 'wynik':"  + wynik;
    console.log("To jest napis w konsoli przeglądarki");
}

// //-->
// </script> */}

// var, let - zmienna można zmieniać dowolnie
// const - stała nie można jej zmienić 


// Typy danych
let liczba = 5; // Liczba całkowita
let liczbaZmiennoprzecinkowa = 3.14; // Liczba zmiennoprzecinkowa
let tekst = "Hello, World!"; // Tekst
let boolean = true; // Wartość logiczna (prawda/fałsz)
let tablica = [1, 2, 3, 4, 5]; // Tablica
let obiekt = { klucz1: "wartość1", klucz2: "wartość2" }; // Obiekt
let array = [1, 2, 3]; // Tablica utworzona za pomocą literału
let set = new Set([1, 2, 3]); // Zbiór (kolekcja unikalnych wartości)   
let bigInt = BigInt(123456789012345678901234567890); // Liczba całkowita o dużej precyzji (BigInt)
let symbol = Symbol("unikalny symbol"); // Symbol (unikalny identyfikator)

// Typy danych specjalne
let nulle = null; // Brak wartości
let niezdefiniowane = undefined; // Niezdefiniowana wartość

// Typy danych złożone/referencyjne (obiekty, funkcje) wiele zmiennych może wskazywać na ten sam obiekt w pamięci komputera.
let funkcja = function() { console.log("To jest funkcja"); }; // Funkcja
let data = new Date(); // Obiekt daty
array = new Array(1, 2, 3); // Tablica utworzona za pomocą konstruktora
set = new Set([1, 2, 3]); // Zbiór
// Map - kolekcja par klucz-wartość
let mapa = new Map();
// Przykład użycia mapy
mapa.set("klucz1", "wartość1");
mapa.set("klucz2", "wartość2");
// Sprawdzenie typu danych
console.log(typeof liczba); // "number"
console.log(typeof tekst); // "string"
console.log(typeof boolean); // "boolean"
console.log(typeof tablica); // "object" (tablice są obiektami w JavaScript)
console.log(typeof obiekt); // "object"
console.log(typeof nulle); // "object" (specjalny przypadek w JavaScript)
console.log(typeof niezdefiniowane); // "undefined"
console.log(typeof funkcja); // "function"
console.log(typeof data); // "object"
console.log(typeof array); // "object"
console.log(typeof set); // "object"
console.log(typeof mapa); // "object"

// Typowanie danych w JavaScript jest dynamiczne, co oznacza, że typy danych mogą się zmieniać w trakcie działania programu.
dynamicValue = 42; // Początkowo liczba
dynamicValue = "Teraz to tekst"; // Teraz tekst 

// Liczby w różnych formatach
// Duże liczby
// W JavaScript liczby są reprezentowane jako liczby zmiennoprzecinkowe podwójnej precyzji (64-bitowe)  
// Można używać BigInt do reprezentowania bardzo dużych liczb całkowitych
let duzaLiczba = BigInt("1234567890123456789012345678901234567890"); // Duża liczba całkowita
const 1e6 = 1000000; // Notacja naukowa dla 1 miliona
const 2e5 = 200000; // Notacja naukowa dla 200 tysięcy 2*100000
// Małe liczby
const 0.000001 = 1e-6; // Notacja naukowa dla 0.000001
const 0.00001 = 1e-5; // Notacja naukowa dla 0.00001

// szesnastkowe, binarne i ósemkowe
const szesnastkowa = 0xFF; // Szesnastkowa (hexadecimal) - 255
const binarna = 0b11111111; // Binarna (binary) - 255
const ósemkowa = 0o377; // Ósemkowa (octal) - 255

// Funkcja Math
// Funkcja Math w JavaScript zawiera wiele przydatnych metod do wykonywania operacji matematycznych
console.log("Zaokrąglenie:", Math.round(4.7)); // Wynik 5
console.log("Pierwiastek kwadratowy:", Math.sqrt(16)); // Wynik 4   
console.log("Potęga:", Math.pow(2, 3)); // Wynik 8 (2 do potęgi 3)
console.log("Losowa liczba:", Math.random()); // Losowa liczba z zakresu 0-1
console.log("Wartość bezwzględna:", Math.abs(-5)); // Wynik 5 (wartość bezwzględna)
console.log("Maksymalna wartość:", Math.max(1, 2, 3)); // Wynik 3 (największa wartość)
console.log("Minimalna wartość:", Math.min(1, 2, 3)); // Wynik 1 (najmniejsza wartość)
console.log("Zwraca najmniejszą liczbę całkowitą większą lub równą podanej liczbie:", Math.ceil(4.1)); // Wynik 5
console.log("Zwraca największą liczbę całkowitą mniejszą lub równą podanej liczbie:", Math.floor(4.9)); // Wynik 4

// Przykład losowa liczba z przedziału
const min = 1;
const max = 10;
const losowaLiczba = Math.floor(Math.random() * (max - min + 1)) + min; // Losowa liczba z zakresu 1-10

// Stringi
const tekst = "Hello, World!";
// Metody stringów
console.log("Długość tekstu:", tekst.length); // Wynik 13
console.log("Pierwszy znak:", tekst.charAt(0)); // Wynik H
console.log("Znajdź indeks znaku:", tekst.indexOf("W")); // Wynik 7 
console.log("Znajdź ostatni indeks znaku:", tekst.lastIndexOf("o")); // Wynik 8
console.log("Zamień tekst:", tekst.replace("World", "JavaScript")); // Wynik Hello, JavaScript!
console.log("Zamień wszystkie wystąpienia tekstu:", tekst.replace(/o/g, "0")); // Wynik Hell0, W0rld!   
console.log("Podziel tekst:", tekst.split(", ")); // Wynik ["Hello", "World!"]
console.log("Zamień tekst na wielkie litery:", tekst.toUpperCase()); // Wynik HELLO, WORLD!
console.log("Zamień tekst na małe litery:", tekst.toLowerCase()); // Wynik hello, world!
console.log("Sprawdź, czy tekst zaczyna się od:", tekst.startsWith("Hello")); // Wynik true
console.log("Sprawdź, czy tekst kończy się na:", tekst.endsWith("!")); // Wynik true
console.log("Wytnij tekst od indeksu 7:", tekst.slice(7)); // Wynik World!
console.log("Wytnij tekst od indeksu 7 do 12:", tekst.slice(7, 12)); // Wynik World
console.log("Wytnij tekst od indeksu 0 do 5:", tekst.substring(0, 5)); // Wynik Hello

// Poruszanie się po znakach w tekście

for (let i = 0; i < tekst.length; i++) {
    console.log("Znak na indeksie " + i + ":", tekst.charAt(i)); // Wyświetla każdy znak w tekście
    console.log( tekst[i]);
}
for (const znak of tekst) {
    console.log("Znak:", znak); // Wyświetla każdy znak w tekście
}

// Zmiana textu
const zmienionyTekst = tekst.replace("World", "JavaScript");
console.log("Zmieniony tekst:", zmienionyTekst); // Wynik Hello, JavaScript!
// lub inny sposób
tablicaTekst = tekst.split(" "); // Podziel tekst na tablicę słów

// Wyświetlenie każdego słowa w tablicy
for (const slowo of tablicaTekst) {
    console.log("Słowo:", slowo);
}
 const tab = [...tekst]; // Przypisanie tekstu do tablicy
 tab[0] = "B"; // Zmiana wartości w tablicy
 const nowyTekst = tab.join[""]; // Połączenie elementów tablicy w jeden tekst
// Wyświetlenie zmienionego tekstu  
console.log("Nowy tekst:", nowyTekst); // Wynik B


// Funkcja replace
// Funkcja replace jest używana do zamiany części tekstu na inny tekst
// Przykład użycia replace  
const oryginalnyTekst = "To jest oryginalny tekst";
const nowyTekst = oryginalnyTekst.replace("oryginalny", "zmieniony");
console.log("Oryginalny tekst:", oryginalnyTekst); // Wynik To jest oryginalny tekst
console.log("Nowy tekst:", nowyTekst); // Wynik To jest zmieniony tekst
// Lub inny sposób
let text= "Ala ma kota";
let nowyText =[...text]; // Przypisanie tekstu do tablicy
console.log("Tablica znaków:", nowyText); // Wynik ["A", "l", "a", " ", "m", "a", " ", "k", "o", "t", "a"]
nowyText[0] = "E"; // Zmiana wartości w tablicy
console.log("Zmieniona tablica znaków:", nowyText); // Wynik ["E", "l", "a", " ", "m", "a", " ", "k", "o", "t", "a"]
// Połączenie elementów tablicy w jeden tekst   
const zmienionyTekst2 = nowyText.join(""); // Połączenie elementów tablicy w jeden tekst
console.log("Zmieniony tekst:", zmienionyTekst2); // Wynik Ela ma kota
let nowyText2 = text.replace(/A/g, "E"); // Zamiana wszystkich wystąpień "A" na "E"
console.log("Zmieniony tekst 2:", nowyText2); // Wynik Ela ma kota

// łamanie textu
const tekstDoZlamania = "To jest bardzo długi tekst, który chcemy złamać na kilka linii, aby był bardziej czytelny.";
const zlamanyTekst = tekstDoZlamania.match(/.{1,30}/g); // Łamanie tekstu co 30 znaków
console.log("Złamany tekst:", zlamanyTekst); // Wynik ["To jest bardzo długi tekst,", "który chcemy złamać na kilka", "linii, aby był bardziej czytelny."]
// lub inny sposób
let tekstDoZlamania2 = "To jest bardzo długi tekst, który chcemy złamać na kilka linii, aby był bardziej czytelny.";
tekstDoZlamania2 += "To jest bardzo długi tekst,<br>";
tekstDoZlamania2 += "który chcemy złamać na kilka linii,<br>";
tekstDoZlamania2 += "aby był bardziej czytelny.";

// Dodawanie elementu do textu
const age = 25;
const tekstZAge = `Mam ${age} lat.`; // Użycie szablonów stringów (template literals)
console.log("Tekst z wiekiem:", tekstZAge); // Wynik Mam 25 lat.
// lub inny sposób  
let wiek = 30;
let tekstZWiekem = "Mam " + wiek + " lat."; // Użycie konkatenacji stringów
console.log("Tekst z wiekiem:", tekstZWiekem); // Wynik Mam 30 lat.


// Pobieranie znaku na danj pozycji 

console.log("Znak na pozycji 0:", tekst.charAt(0)); // Wynik H
console.log("Znak na pozycji 4:", tekst.charAt(4)); // Wynik o

// Pobieranie znaku na danej pozycji w tablicy
const tablicaZnakow = [...tekst]; // Przypisanie tekstu do tablicy znaków
console.log("Znak na pozycji 0 w tablicy:", tablicaZnakow[0]); // Wynik H
console.log("Znak na pozycji 4 w tablicy:", tablicaZnakow[4]); // Wynik o

console.log(tekst.charAt(tekst.length - 1)); // Pobranie ostatniego znaku w tekście
console.log(tablicaZnakow[tablicaZnakow.length - 1]); // Pobranie ostatniego znaku w tablicy znaków

// Funkcja UpperCase i LowerCase
// Funkcja toUpperCase() zamienia wszystkie znaki w tekście na wielkie litery
// Funkcja toLowerCase() zamienia wszystkie znaki w tekście na małe litery
const tekstDuzeLitery = tekst.toUpperCase(); // Zamiana na wielkie litery
const tekstMaleLitery = tekst.toLowerCase(); // Zamiana na małe litery
console.log("Tekst z wielkimi literami:", tekstDuzeLitery); // Wynik HELLO, WORLD!
console.log("Tekst z małymi literami:", tekstMaleLitery); // Wynik hello, world!

// Funkcja indexOf i lastIndexOf
// Funkcja indexOf() zwraca indeks pierwszego wystąpienia podanego znaku lub tekstu
// Funkcja lastIndexOf() zwraca indeks ostatniego wystąpienia podanego znaku lub tekstu
const tekstDoSzukania = "To jest tekst do szukania. To jest tekst do szukania.";
const indeksPierwszegoWystapienia = tekstDoSzukania.indexOf("tekst"); // Indeks pierwszego wystąpienia "tekst"
const indeksOstatniegoWystapienia = tekstDoSzukania.lastIndexOf("tekst"); // Indeks ostatniego wystąpienia "tekst"
console.log("Indeks pierwszego wystąpienia 'tekst':", indeksPierwszegoWystapienia); // Wynik 6
console.log("Indeks ostatniego wystąpienia 'tekst':", indeksOstatniegoWystapienia); // Wynik 30

// Funkcja startsWith i endsWith
// Funkcja startsWith() sprawdza, czy tekst zaczyna się od podanego znaku lub tekstu
// Funkcja endsWith() sprawdza, czy tekst kończy się na podanym znaku lub tekście
const tekstDoSprawdzenia = "To jest tekst do sprawdzenia.";
const czyZaczynaSieOd = tekstDoSprawdzenia.startsWith("To"); // Sprawdzenie, czy tekst zaczyna się od "To"
const czyKonczySieNa = tekstDoSprawdzenia.endsWith("."); // Sprawdzenie, czy tekst kończy się na "." (true)
console.log("Czy tekst zaczyna się od 'To':", czyZaczynaSieOd); // Wynik true
console.log("Czy tekst kończy się na '.':", czyKonczySieNa); // Wynik true

// Funkcja substring i length
// Funkcja substring() zwraca część tekstu od podanego indeksu początkowego do końcowego
// Funkcja length zwraca długość tekstu
const tekstDoPodzialu = "To jest tekst do podziału.";
const podzielonyTekst = tekstDoPodzialu.substring(0, 10); // Podział tekstu od indeksu 0 do 10
const dlugoscTekstu = tekstDoPodzialu.length; // Długość tekstu
console.log("Podzielony tekst:", podzielonyTekst); // Wynik To jest tekst
console.log("Długość tekstu:", dlugoscTekstu); // Wynik 27

// Funkcja slice
// Funkcja slice() zwraca część tekstu od podanego indeksu początkowego do końcowego
const tekstDoWycięcia = "To jest tekst do wycięcia.";
const wycietyTekst = tekstDoWycięcia.slice(0, 10); // Wycięcie tekstu od indeksu 0 do 10
console.log("Wycięty tekst:", wycietyTekst); // Wynik To jest teks

// Funkcja split
// Funkcja split() dzieli tekst na tablicę elementów na podstawie podanego separatora
const tekstDoPodzialu2 = "To jest tekst do podziału.";
const podzielonyTekst2 = tekstDoPodzialu2.split(" "); // Podział tekstu na słowa
console.log("Podzielony tekst na słowa:", podzielonyTekst2); // Wynik ["To", "jest", "tekst", "do", "podziału."]


// Operatory arytmetyczne
const x = 10;
const y = 5;

console.log("Dodawanie:", x + y); // Wynik 15
console.log("Odejmowanie:", x - y); // Wynik 5
console.log("Mnożenie:", x * y); // Wynik 50
console.log("Dzielenie:", x / y); // Wynik 2
console.log("Modulo:", x % y); // Wynik 0
console.log("Potęgowanie:", x ** y); // Wynik 100000
// Operatory porównania
console.log("Równość:", x == y); // Wynik false
console.log("Równość ścisła:", x === y); // Wynik false
console.log("Nierówność:", x != y); // Wynik true
console.log("Nierówność ścisła:", x !== y); // Wynik true
console.log("Większe:", x > y); // Wynik true
console.log("Mniejsze:", x < y); // Wynik false
console.log("Większe lub równe:", x >= y); // Wynik true
console.log("Mniejsze lub równe:", x <= y); // Wynik false
// Operatory przypisania
let a1 = 10;
let b1 = 5;
a1 += b1; // a1 = a1 + b1
console.log("Przypisanie z dodaniem:", a1); // Wynik 15
a1 -= b1; // a1 = a1 - b1
console.log("Przypisanie z odejmowaniem:", a1); // Wynik 10
a1 *= b1; // a1 = a1 * b1
console.log("Przypisanie z mnożeniem:", a1); // Wynik 50
a1 /= b1; // a1 = a1 / b1
console.log("Przypisanie z dzieleniem:", a1); // Wynik 10
a1 %= b1; // a1 = a1 % b1
console.log("Przypisanie z modulo:", a1); // Wynik 0
a1 **= b1; // a1 = a1 ** b1
console.log("Przypisanie z potęgowaniem:", a1); // Wynik 0
// Operatory bitowe
// Operatory bitowe działają na liczbach jako na ciągach bitów
// Operatory bitowe są używane do manipulacji bitami liczb całkowitych


// Operatory logiczne
const a = 5;
const b = 3;
console.log("Logiczne AND", a&b)
// Wynik 1
console.log("Logiczne |", a|b)
// Wynik 7
console.log("Logiczne XOR", a^b)
// Wynik 6
console.log("Logiczne ~", ~a)
// Wynik -6
console.log("Logiczne <<", a<<b)
// Wynik 40
console.log("Logiczne >>", a>>b)
// Wynik 0
console.log("Logiczne >>>", a>>>b)
// Wynik 0

// Typy mutowalne i niemutowalne
// Typy mutowalne: tablice, obiekty
// Typy niemutowalne: liczby, stringi, boolean, null, undefined, symbol, BigInt 
// Typy mutowalne można zmieniać, dodawać lub usuwać elementy
// Typy niemutowalne nie można zmieniać, można tylko tworzyć nowe wartości  
// przykład mutowalności
let tablicaMutowalna = [1, 2, 3];   
tablicaMutowalna.push(4); // Dodanie elementu do tablicy
console.log(tablicaMutowalna); // Wynik: [1, 2, 3, 4]   
// przykład niemutowalności
let tekstNiemutowalny = "Hello";
tekstNiemutowalny = tekstNiemutowalny + " World"; // Tworzenie nowego stringa
console.log(tekstNiemutowalny); // Wynik: "Hello World"

//  Obiekty i tablice
// Obiekty są kolekcjami par klucz-wartość, gdzie klucze są unikalne
let obiekt = {
    imie: "Jan",
    nazwisko: "Kowalski",
    wiek: 30,
    adres: {
        ulica: "Kwiatowa",
        miasto: "Warszawa"
    }
};
// Dostęp do wartości w obiekcie
console.log("Imię:", obiekt.imie); // Wynik: Jan
console.log("Nazwisko:", obiekt.nazwisko); // Wynik: Kowalski
console.log("Wiek:", obiekt.wiek); // Wynik: 30
console.log("Ulica:", obiekt.adres.ulica); // Wynik: Kwiatowa
console.log("Miasto:", obiekt.adres.miasto); // Wynik: Warszawa

// Dostęp do wartości w obiekcie za pomocą klucza
obiekt.imie = "Anna"; // Zmiana wartości klucza 'imie'
console.log("Nowe imię:", obiekt.imie); // Wynik: Anna


// Tablice są dynamicznymi strukturami danych, które mogą przechowywać wiele wartości
// Tablice są uporządkowanymi kolekcjami wartości, które mogą być różnych typów
let tablica = [1, "dwa", true, { klucz: "wartość" }, [5, 6, 7]];
// Dostęp do wartości w tablicy
console.log("Pierwszy element tablicy:", tablica[0]); // Wynik: 1
console.log("Drugi element tablicy:", tablica[1]); // Wynik: dwa
console.log("Trzeci element tablicy:", tablica[2]); // Wynik: true
console.log("Czwarty element tablicy:", tablica[3].klucz); // Wynik: wartość
console.log("Piąty element tablicy:", tablica[4][0]); // Wynik: 5



// Instrukcje warunkowe

const mojaStala = 8;
// if (mojaStala === 10) {ten kawałek kodu się nie wykona}
if (mojaStala <= 10) {console.log(mojaStala + "ten się wykona")}
console.log(mojaStala)

// switch

godz=(prompt("Ile godzin spędzasz na czacie?"));
switch(godz)
{
    case 0: napis="Nie wiesz co to jest?";
break;
    case 1: napis="To w zupełności wystarczy";
break;
    case 2: napis="Jesteś maniakiem";
break;
    default: napis="Powinieneś się leczyć";
break;

}
console.log(napis)


// pętle

let wynik="";
for (let i = 0; i < 10; i++) {
    wynik += i;
}
document.getElementById("wynik").innerHTML = wynik;


// Pętla If
// Pętla if jest używana do wykonywania kodu, jeśli warunek jest prawdziwy
let petla_If = 0;
let tekstHTMLIf = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
if (petla_If < 5) {
    console.log("Pętla If wykonuje się, ponieważ warunek jest prawdziwy");
    tekstHTMLIf += "Pętla If wykonuje się, ponieważ warunek jest prawdziwy<br>";
    petla_If++;
}
document.getElementById("petla_If").innerHTML = tekstHTMLIf + 'Ile razy wykonała się pętla If: ' + petla_If;


// Pętla If Else
// Pętla if else jest używana do wykonywania kodu, jeśli warunek jest prawdziwy lub fałszywy
let petla_IfElse = 0;
let tekstHTMLIfElse = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
if (petla_IfElse < 5) {
    console.log("Pętla If Else wykonuje się, ponieważ warunek jest prawdziwy");
    tekstHTMLIfElse += "Pętla If Else wykonuje się, ponieważ warunek jest prawdziwy<br>";
    petla_IfElse++;
}  
else {
    console.log("Pętla If Else nie wykonuje się, ponieważ warunek jest fałszywy");
    tekstHTMLIfElse += "Pętla If Else nie wykonuje się, ponieważ warunek jest fałszywy<br>";
}
document.getElementById("petla_IfElse").innerHTML = tekstHTMLIfElse + 'Ile razy wykonała się pętla If Else: ' + petla_IfElse;

// Pętla Switch
// Pętla switch jest używana do wykonywania kodu w zależności od wartości zmiennej
let petla_Switch = 0;
let tekstHTMLSwitch = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
switch (petla_Switch) {
    case 0:
        console.log("Pętla Switch wykonuje się, ponieważ wartość jest równa 0");
        tekstHTMLSwitch += "Pętla Switch wykonuje się, ponieważ wartość jest równa 0<br>";
        petla_Switch++;
        break;
    case 1:
        console.log("Pętla Switch nie wykonuje się, ponieważ wartość jest równa 1");
        tekstHTMLSwitch += "Pętla Switch nie wykonuje się, ponieważ wartość jest równa 1<br>";
        break;
    default:
        console.log("Pętla Switch nie wykonuje się, ponieważ wartość jest inna niż 0 lub 1");
        tekstHTMLSwitch += "Pętla Switch nie wykonuje się, ponieważ wartość jest inna niż 0 lub 1<br>";
}   
document.getElementById("petla_Switch").innerHTML = tekstHTMLSwitch + 'Ile razy wykonała się pętla Switch: ' + petla_Switch;

// Pętla Ternary
// Pętla ternary jest skróconą formą instrukcji if else
let petla_Ternary = 0;
let tekstHTMLTernary = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
petla_Ternary = (petla_Ternary < 5) ? "Pętla Ternary wykonuje się, ponieważ warunek jest prawdziwy" : "Pętla Ternary nie wykonuje się, ponieważ warunek jest fałszywy";
console.log(petla_Ternary);
tekstHTMLTernary += petla_Ternary + "<br>"; // Dodaj wartość i znacznik nowej linii
document.getElementById("petla_Ternary").innerHTML = tekstHTMLTernary + 'Ile razy wykonała się pętla Ternary: ' + petla_Ternary;



// Pętla for
// Pętla for jest używana do iteracji po liczbach lub tablicach
let petla_For = 0;
let tekstHTMLFor = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
for (let i = 0; i < 5; i++) {
    console.log(i);
    tekstHTMLFor += i + "<br>"; // Dodaj wartość i znacznik nowej linii
    petla_For++;
}
document.getElementById("petla_For").innerHTML = tekstHTMLFor + 'Ile razy wykonała się pętla For: ' + petla_For;

// Pętla for in
// Pętla for in jest używana do iteracji po właściwościach obiektu
let obiekt = {a: 1, b: 2, c: 3};
let tekstHTMLForIn = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
for (let klucz in obiekt) {
    console.log(klucz + ": " + obiekt[klucz]);
    tekstHTMLForIn += klucz + ": " + obiekt[klucz] + "<br>"; // Dodaj wartość i znacznik nowej linii
}
document.getElementById("petla_ForIn").innerHTML = tekstHTMLForIn + 'Ile razy wykonała się pętla For In: ' + Object.keys(obiekt).length;


// Pętla for of
// Pętla for of jest używana do iteracji po elementach kolekcji, takich jak tablice
let tablica = [1, 2, 3, 4, 5];
let tekstHTMLForOf = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
for (let wartosc of tablica) {
    console.log(wartosc);
    tekstHTMLForOf += wartosc + "<br>"; // Dodaj wartość i znacznik nowej linii
}
document.getElementById("petla_ForOf").innerHTML = tekstHTMLForOf + 'Ile razy wykonała się pętla For Of: ' + tablica.length;


// Pętla while
// Pętla while wykonuje się dopóki warunek jest prawdziwy

let petla_While = 0;
let tekstHTML = ""; // Zmienna do zbierania wartości do wyświetlenia w HTML
while (petla_While < 5) {
    console.log(petla_While);
    tekstHTML += petla_While + "<br>"; // Dodaj wartość i znacznik nowej linii
    petla_While++;
}
document.getElementById("petla_While").innerHTML = tekstHTML + 'Ile razy wykonała się pętla While: ' + petla_While;

// Pętla do while
// Pętla do while wykonuje się przynajmniej raz, nawet jeśli warunek jest fałszywy
let petla_DoWhile = 0;
do {
  console.log(petla_DoWhile);
  petla_DoWhile++;
} while (petla_DoWhile < 5);
document.getElementById("petla_DoWhile").innerHTML = "Pętla do while: " + petla_DoWhile;


// funkcje

function dodaj(a, b) {
    return a + b;
}


function mnoz(a, b) {
    return a * b;
}


function dziel(a, b) {
    if (b === 0) {
        console.error("Nie można dzielić przez zero");
        return null;
    }
    return a / b;
}


function odejmij(a, b) {
    return a - b;
}


function potega(a, b) {
    return Math.pow(a, b);
}


function pierwiastek(a) {
    if (a < 0) {
        console.error("Nie można obliczyć pierwiastka z liczby ujemnej");
        return null;
    }
    return Math.sqrt(a);
}


function silnia(n) {
    if (n < 0) {
        console.error("Nie można obliczyć silni z liczby ujemnej");
        return null;
    }
    if (n === 0 || n === 1) {
        return 1;
    }
    let wynik = 1;
    for (let i = 2; i <= n; i++) {
        wynik *= i;
    }
    return wynik;
}


function liczbyPierwsze(n) {
    if (n < 2) {
        return [];
    }
    const primes = [];
    for (let i = 2; i <= n; i++) {
        let isPrime = true;
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push(i);
        }
    }
    return primes;
}


function fibonacci(n) {
    if (n < 0) {
        console.error("Nie można obliczyć ciągu Fibonacciego dla liczby ujemnej");
        return null;
    }
    const fib = [0, 1];
    for (let i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib.slice(0, n);
}


function odwrocTekst(tekst) {
    return tekst.split('').reverse().join('');
}


function palindrom(tekst) {
    const odwrocony = odwrocTekst(tekst);
    return tekst === odwrocony;
}


function anagram(tekst1, tekst2) {
    const sortuj = (tekst) => tekst.split('').sort().join('');
    return sortuj(tekst1) === sortuj(tekst2);
}


function liczbaPierwsza(n) {
    if (n < 2) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}


function liczbyDoskonale(n) {
    const doskonale = [];
    for (let i = 1; i <= n; i++) {
        let sumaDzielnikow = 0;
        for (let j = 1; j < i; j++) {
            if (i % j === 0) {
                sumaDzielnikow += j;
            }
        }
        if (sumaDzielnikow === i) {
            doskonale.push(i);
        }
    }
    return doskonale;
}


function liczbyZlozone(n) {
    const zlozone = [];
    for (let i = 4; i <= n; i++) {
        let jestZlozona = false;
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                jestZlozona = true;
                break;
            }
        }
        if (jestZlozona) {
            zlozone.push(i);
        }
    }
    return zlozone;
}

function liczbyPierwszeDoN(n) {
    const primes = [];
    for (let i = 2; i <= n; i++) {
        let isPrime = true;
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push(i);
        }
    }
    return primes;
}



function liczbyDoskonaleDoN(n) {
    const doskonale = [];
    for (let i = 1; i <= n; i++) {
        let sumaDzielnikow = 0;
        for (let j = 1; j < i; j++) {
            if (i % j === 0) {
                sumaDzielnikow += j;
            }
        }
        if (sumaDzielnikow === i) {
            doskonale.push(i);
        }
    }
    return doskonale;
}

// Funkcja getArea przyjmuje dwa argumenty: szerokość i wysokość, a następnie zwraca pole prostokąta.

function getArea(width, height) {
    return width * height;
}
getArea(5, 10); // Wynik 50

// Funkcje wymagające informacji (argumentów) są bardziej elastyczne i mogą być używane w różnych kontekstach, ponieważ przyjmują różne wartości wejściowe.
// Funkcje bez argumentów są bardziej statyczne i nie mogą być używane w różnych kontekstach, ponieważ zawsze zwracają tę samą wartość.

function calcArea(width, height) {
    return width * height;
}
var areaOne = calcArea(5, 10); // Wynik 50
var areaTwo = calcArea(7, 3); // Wynik 21
// Funkcje są blokami kodu, które można wielokrotnie wywoływać
// Funkcje mogą przyjmować argumenty i zwracać wartości
// Funkcje mogą być anonimowe i przypisane do zmiennych
// Funkcje mogą być zdefiniowane jako funkcje strzałkowe (arrow functions) lub tradycyjne funkcje
// Funkcje mogą być zagnieżdżone, co oznacza, że jedna funkcja może wywoływać inną funkcję
// Funkcje mogą być przekazywane jako argumenty do innych funkcji
// Funkcje mogą być zwracane z innych funkcji, co pozwala na tworzenie funkcji wyższego rzędu
// Funkcje mogą być używane do tworzenia modułów, które grupują powiązane funkcje i zmienne
// Funkcje mogą być używane do tworzenia klas i obiektów, które grupują powiązane funkcje i zmienne
// Funkcje mogą być używane do tworzenia zdarzeń, które reagują na interakcje użytkownika
// Funkcje mogą być używane do tworzenia asynchronicznych operacji, które wykonują się w tle i nie blokują głównego wątku programu
// Zwrot wielu wartości z funkcji
function getSize(width, height, depth) {
    var area = width * height; // Oblicza pole
    var volume = width * height * depth; // Oblicza pole i objętość
    var size = [area, volume]; // Tworzy tablicę z polem i objętością
    return size; // Zwraca tablicę z polem i objętością
}
var areaTry = getSize(5, 10, 2) [0]; // Wywołuje funkcję i przypisuje wynik do zmiennej areaTry
var volumeTwo = getSize(5, 10, 2) [1]; // Wywołuje funkcję i przypisuje wynik do zmiennej volumeTwo
// console.log("Pole:", areaTry); // Wynik 50
// console.log("Objętość:", volumeTwo); // Wynik 100
// Parametry a argumenty funkcji
// Parametry to zmienne, które są zdefiniowane w funkcji i służą do przyjmowania wartości wejściowych   
// Argumenty to wartości, które są przekazywane do funkcji podczas jej wywołania
// Parametry są używane do definiowania funkcji, a argumenty są używane do wywoływania funkcji
// Przykład funkcji z parametrami i argumentami

function przykladFunkcji(parametr1, parametr2) {
    return parametr1 + parametr2;
}
var wynik = przykladFunkcji(5, 10); // Wywołanie funkcji z argumentami 5 i 10
console.log("Wynik:", wynik); // Wynik 15


function args() {
    return arguments; // Funkcja zwraca argumenty przekazane do niej
}
console.log(args()); // Wynik [Arguments] - obiekt zawierający argumenty przekazane do funkcji
console.log(args(1, 2, 3)); // Wynik [1, 2, 3] - argumenty przekazane do funkcji


// Funkcje strzałkowe (arrow functions) 
// Funkcje strzałkowe to skrócona składnia funkcji w JavaScript, która pozwala na tworzenie funkcji bez użycia słowa kluczowego 'function'
const dodajStrzalkowo = (a, b) => a + b; // Funkcja strzałkowa do dodawania dwóch liczb
const mnozStrzalkowo = (a, b) => a * b; // Funkcja strzałkowa do mnożenia dwóch liczb   
const dzielStrzalkowo = (a, b) => {
    if (b === 0) {
        console.error("Nie można dzielić przez zero");
        return null;
    }
    return a / b;
}   
const odejmijStrzalkowo = (a, b) => a - b; // Funkcja strzałkowa do odejmowania dwóch liczb

// Funkcje anonimowe
// Funkcje anonimowe to funkcje, które nie mają nazwy i są często używane jako argumenty dla innych funkcji
const dodajAnonimowo = function(a, b) {
    return a + b; // Funkcja anonimowa do dodawania dwóch liczb
}   
const mnozAnonimowo = function(a, b) {
    return a * b; // Funkcja anonimowa do mnożenia dwóch liczb
}
// Funkcje zagnieżdżone
// Funkcje zagnieżdżone to funkcje, które są zdefiniowane wewnątrz innych funkcji
function zagniezdzonaFunkcja() {
    const wewnetrznaFunkcja = (a, b) => a + b; // Funkcja zagnieżdżona do dodawania dwóch liczb
    return wewnetrznaFunkcja(5, 10); // Wywołanie funkcji zagnieżdżonej
}
console.log("Wynik funkcji zagnieżdżonej:", zagniezdzonaFunkcja()); // Wynik 15
// Funkcje wyższego rzędu
// Funkcje wyższego rzędu to funkcje, które mogą przyjmować inne funkcje jako argumenty lub zwracać funkcje jako wynik
function funkcjaWyższegoRzedu(funkcja, a, b) {
    return funkcja(a, b);
}
console.log("Wynik funkcji wyższego rzędu:", funkcjaWyższegoRzedu(dodajStrzalkowo, 5, 10)); // Wynik 15

function sum () {
    console.log(arguments); // Wyświetla wszystkie argumenty przekazane do funkcji
}
sum(1, 2, 3); // Wywołanie funkcji z argumentami 1, 2, 3
sum("ala", "ma", "kota"); // Wywołanie funkcji z argumentami "ala", "ma", "kota"


function print(name = "Paweł", status = "najlepszym programista") {
    console.log(name + " jest " + status);
}

print(); // Wywołanie funkcji bez argumentów, użyje domyślnych wartości
print("Jan"); // Wywołanie funkcji z argumentami, nadpisze domyślne wartości
print("Michał", "wysoki"); // Wywołanie funkcji z argumentami, nadpisze domyślne wartości
print(undefined, "programistą"); // Wywołanie funkcji z jednym argumentem, drugi użyje domyślnej wartości

// Parametry reszty
// Parametry reszty to specjalny typ parametru, który pozwala na przekazywanie nieokreślonej liczby argumentów do funkcji

function superSum(...r) {
    console.log(r); // Wyświetla wszystkie argumenty przekazane do funkcji
}
superSum(1, 2, 3); // Wywołanie funkcji z argumentami 1, 2, 3

// lub 

function suma(...liczby) {
    return liczby.reduce((acc, curr) => acc + curr, 0);
}
console.log("Suma:", suma(1, 2, 3, 4, 5)); // Wynik 15

// Funkcje rekurencyjne
// Funkcje rekurencyjne to funkcje, które wywołują same siebie w celu rozwiązania problemu
function silniaRekurencyjna(n) {
    if (n === 0) {
        return 1;
    }
    return n * silniaRekurencyjna(n - 1);
}

console.log("Silnia rekurencyjna z 5:", silniaRekurencyjna(5)); // Wynik 120


// Funkcje asynchroniczne
// Funkcje asynchroniczne to funkcje, które wykonują się w tle i nie blokują głównego wątku programu
async function pobierzDane() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        console.log("Dane:", data);
    } catch (error) {
        console.error("Błąd podczas pobierania danych:", error);
    }
}

// Wywołanie funkcji asynchronicznej
pobierzDane(); // Wywołanie funkcji asynchronicznej, która pobiera dane z API

// Zmienne globalne i lokalne
// Zmienne globalne są dostępne w całym kodzie, natomiast zmienne lokalne są dostępne tylko w obrębie funkcji lub bloku kodu, w którym zostały zdefiniowane
let zmiennaGlobalna = "Jestem zmienną globalną"; // Zmienna globalna
function funkcjaLokalna() {
    let zmiennaLokalna = "Jestem zmienną lokalną"; // Zmienna lokalna
}
console.log(zmiennaGlobalna); // Wyświetla zmienną globalną
// console.log(zmiennaLokalna); // Błąd: zmiennaLokalna nie jest zdefiniowana, ponieważ jest lokalna

var global =1;
function test() {
    var local = 2; // Zmienna lokalna
    global++; // Zmienna globalna
    return global; // Zwraca zmienną globalną
}
console.log("Wynik funkcji test:", test()); // Wynik 2

// Wynoszenie zmiennych
// Wynoszenie zmiennych (hoisting) to mechanizm w JavaScript, który polega na przenoszeniu deklaracji zmiennych i funkcji na początek ich zakresu
// Zmienne zadeklarowane za pomocą var są wynoszone na początek funkcji lub globalnego zakresu
var zmiennaWynoszona = "Jestem wynoszoną zmienną"; // Zmienna wynoszona
function funkcjaWynoszona() {
    alert(zmiennaWynoszona);
    var zmiennaWynoszona = "Zmienna wynoszona w funkcji"; // Zmienna wynoszona w funkcji
    alert(zmiennaWynoszona); // Wyświetla zmienną wynoszoną w funkcji
}
funkcjaWynoszona(); // Wywołanie funkcji, która wyświetla zmienną wynoszoną w funkcji


// Zmienne blokowe
// Zmienne blokowe są dostępne tylko w obrębie bloku kodu, w którym zostały zdefiniowane
var A = 1;
{
    let A = "Jestem zmienną blokową"; // Zmienna blokowa
    console.log(A); // Wyświetla zmienną blokową
}
console.log(A); // Wyświetla zmienną globalną, ponieważ zmienna blokowa jest dostępna tylko w obrębie bloku kodu

// Funkcje anonimowe
// Funkcje anonimowe to funkcje, które nie mają nazwy i są często używane jako argumenty dla innych funkcji
var f = function(a) {
    return a * 2;
};
// Wywołanie funkcji anonimowej
console.log("Wynik funkcji anonimowej:", f(5)); // Wynik 10

// Wywołanie zwrotne
// Wywołanie zwrotne (callback) to funkcja, która jest przekazywana jako argument do innej funkcji i jest wywoływana po zakończeniu działania tej funkcjifunt

function invokeAdd(a, b) {
    return a() + b(); // Funkcja zwrotna do dodawania dwóch liczb
}
function one () {
    return 1; // Funkcja zwrotna zwracająca 1
}

function two () {
    return 2; // Funkcja zwrotna zwracająca 2
}
// Wywołanie funkcji zwrotnej
console.log("Wynik wywołania zwrotnego:", invokeAdd(one, two)); // Wynik 3

// Funkcje wewnętrzne (prywatne)
function outr(param) {
    function inner(theinput) {
        return input * 2; // Funkcja wewnętrzna do mnożenia przez 2
    }
return "Wynik funkcji wewnętrznej: " + inner(param); // Wywołanie funkcji wewnętrznej
}
console.log(outr(5)); // Wywołanie funkcji wewnętrznej, wynik 10

// TABLICE

// Tworzenie tablicy
const tablica1 = [1, 2, 3, 4, 5];
console.log("Tablica:", tablica1);

// Dodawanie elementów do tablicy
tablica1.push(6); // Dodanie elementu na końcu tablicy  
console.log("Tablica po dodaniu elementu:", tablica1); // Wynik [1, 2, 3, 4, 5, 6]
tablica1.unshift(0); // Dodanie elementu na początku tablicy
console.log("Tablica po dodaniu elementu na początku:", tablica1); // Wynik [0, 1, 2, 3, 4, 5, 6]
// Usuwanie elementów z tablicy
tablica1.pop(); // Usunięcie ostatniego elementu z tablicy
console.log("Tablica po usunięciu ostatniego elementu:", tablica1); // Wynik [0, 1, 2, 3, 4, 5]
tablica1.shift(); // Usunięcie pierwszego elementu z tablicy
console.log("Tablica po usunięciu pierwszego elementu:", tablica1); // Wynik [1, 2, 3, 4, 5]
// Modyfikowanie elementów w tablicy
tablica1[0] = 10; // Zmiana wartości pierwszego elementu tablicy
console.log("Tablica po zmianie pierwszego elementu:", tablica1); // Wynik [10, 2, 3, 4, 5]
// Iterowanie po tablicy
for (let i = 0; i < tablica1.length; i++) {
    console.log("Element na indeksie " + i + ":", tablica1[i]); // Wyświetla każdy element w tablicy
}
// Enumerowanie tablicy
for (const element of tablica1) {
    console.log("Element:", element); // Wyświetla każdy element w tablicy
}
// Sprawdzanie długości tablicy
console.log("Długość tablicy:", tablica1.length); // Wynik 5    
// Łączenie tablic
const tablica2 = [6, 7, 8];
const polaczonaTablica = tablica1.concat(tablica2); // Łączenie dwóch tablic
console.log("Połączona tablica:", polaczonaTablica); // Wynik [10, 2, 3, 4, 5, 6, 7, 8]
// Sprawdzanie, czy tablica zawiera dany element
console.log("Czy tablica zawiera 3?", tablica1.includes(3)); // Wynik true
// Sprawdzanie indeksu elementu w tablicy
console.log("Indeks elementu 3:", tablica1.indexOf(3)); // Wynik 2
// Sprawdzanie ostatniego indeksu elementu w tablicy
console.log("Ostatni indeks elementu 3:", tablica1.lastIndexOf(3)); // Wynik 2
// Odwracanie tablicy
const odwroconaTablica = tablica1.slice().reverse(); // Odwracanie tablicy
console.log("Odwrócona tablica:", odwroconaTablica); // Wynik [5, 4, 3, 2, 10]
// Sortowanie tablicy
const posortowanaTablica = tablica1.slice().sort((a, b) => a - b); // Sortowanie tablicy rosnąco
console.log("Posortowana tablica:", posortowanaTablica); // Wynik [2, 3, 4, 5, 10]
// Spłaszczanie tablicy
const zagniezdzonaTablica = [1, [2, 3], [4, 5]];
const splaszczonaTablica = zagniezdzonaTablica.flat();
console.log("Spłaszczona tablica:", splaszczonaTablica); // Wynik [1, 2, 3, 4, 5]
// Mapowanie tablicy
const tablicaMap = [1, 2, 3, 4, 5];
const podwojonaTablica = tablicaMap.map(element => element * 2); // Podwajanie każdego elementu tablicy
console.log("Podwojona tablica:", podwojonaTablica); // Wynik [2, 4, 6, 8, 10]

// Pętla for .. of
const tablicaForOf = [1, 2, 3, 4, 5];
for (const element of tablicaForOf) {
    console.log("Element w pętli for .. of:", element); // Wyświetla każdy element w tablicy
}   
// lub inny sposób

const countries = ["Polska", "Niemcy", "Francja", "Hiszpania"];
for (const country of countries) {
    console.log("Kraj:", country.toUpperCase()); // Wyświetla każdy kraj w tablicy
}
// Pętla forEach
const tablicaForEach = [1, 2, 3, 4, 5];
tablicaForEach.forEach((element, index) => {
    console.log(`Element na indeksie ${index}:`, element); // Wyświetla każdy element w tablicy z jego indeksem
});

// Wypełnienie tablicy  
const tab1 = new Array(20); // Tworzenie tablicy o długości 5 wypełnionej zerami
console.log("Pusta tablica:", tab1); // Wynik [undefined, undefined, undefined, undefined, undefined]
tab1.fill(0); // Wypełnienie tablicy zerami
console.log("Tablica wypełniona zerami:", tab1); // Wynik [0, 0, 0, 0, 0]
// Wypełnienie tablicy liczbami od 1 do 20
for (let i = 0; i < tab1.length; i++) {
    tab1[i] = i + 1;
}
console.log("Tablica wypełniona liczbami od 1 do 20:", tab1); // Wynik [1, 2, 3, ..., 20]

// Wypełnienie tablicy losowymi liczbami
const tablicaLosowa = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100)); // Tworzenie tablicy o długości 10 z losowymi liczbami od 0 do 99
console.log("Tablica losowa:", tablicaLosowa);


// Tablice wielowymiarowe   
// Tworzenie tablicy dwuwymiarowej
const tablicaDwuwymiarowa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
console.log("Tablica dwuwymiarowa:", tablicaDwuwymiarowa); // Wynik [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

var tablica3 = [];
// deklaracja drugiego wymiaru
for (var i = 0; i < iloscWierszy; i++) {
    tablica3[i] = [];
}
// wypełnienie tablicy
for (var i = 0; i < iloscWierszy; i++) {
    for (var j = 0; j < iloscKolumn; j++) {
        tablica3[i][j] = i + j;
    }
}

// Dostęp do elementów tablicy dwuwymiarowej
console.log("Element w pierwszym wierszu i pierwszej kolumnie:", tablicaDwuwymiarowa[0][0]); // Wynik 1
console.log("Element w drugim wierszu i trzeciej kolumnie:", tablicaDwuwymiarowa[1][2]); // Wynik 6
// Iterowanie po tablicy dwuwymiarowej
for (var i = 0; i < iloscWierszy; i++) {
    for (var j = 0; j < iloscKolumn; j++) {
        console.log("Element w wierszu " + i + " i kolumnie " + j + ":", tablica3[i][j]);
    }
}
// Spłaszczanie tablicy dwuwymiarowej
const spłaszczonaTablicaDwuwymiarowa = tablicaDwuwymiarowa.flat(); // Spłaszczanie tablicy dwuwymiarowej
console.log("Spłaszczona tablica dwuwymiarowa:", spłaszczonaTablicaDwuwymiarowa); // Wynik [1, 2, 3, 4, 5, 6, 7, 8, 9]
// Łączenie tablicy dwuwymiarowej
const tablicaDwuwymiarowa2 = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
];
const polaczonaTablicaDwuwymiarowa = tablicaDwuwymiarowa.concat(tablicaDwuwymiarowa2); // Łączenie dwóch tablic dwuwymiarowych
console.log("Połączona tablica dwuwymiarowa:", polaczonaTablicaDwuwymiarowa); // Wynik [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
// Sprawdzanie, czy tablica dwuwymiarowa zawiera dany element
console.log("Czy tablica dwuwymiarowa zawiera 5?", tablicaDwuwymiarowa.some(wiersz => wiersz.includes(5))); // Wynik true
// Sprawdzanie indeksu elementu w tablicy dwuwymiarowej
console.log("Indeks elementu 5:", tablicaDwuwymiarowa.findIndex(wiersz => wiersz.includes(5))); // Wynik 1
// Sprawdzanie ostatniego indeksu elementu w tablicy dwuwymiarowej
console.log("Ostatni indeks elementu 5:", tablicaDwuwymiarowa.findLastIndex(wiersz => wiersz.includes(5))); // Wynik 1
// Odwracanie tablicy dwuwymiarowej
const odwroconaTablicaDwuwymiarowa = tablicaDwuwymiarowa.map(wiersz => wiersz.slice().reverse()); // Odwracanie każdego wiersza tablicy dwuwymiarowej
console.log("Odwrócona tablica dwuwymiarowa:", odwroconaTablicaDwuwymiarowa); // Wynik [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
// Sortowanie tablicy dwuwymiarowej
const posortowanaTablicaDwuwymiarowa = tablicaDwuwymiarowa.map(wiersz => wiersz.slice().sort((a, b) => a - b)); // Sortowanie każdego wiersza tablicy dwuwymiarowej rosnąco
console.log("Posortowana tablica dwuwymiarowa:", posortowanaTablicaDwuwymiarowa); // Wynik [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
