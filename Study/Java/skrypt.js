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

// Przykład
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


