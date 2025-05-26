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
// var zmienna="Java Script";
// alert("Witaj"+zmienna);
// //-->
// </script> */}

// var, let - zmienna można zmieniać dowolnie
// const - stała nie można jej zmienić 


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

// while (i < 10) {
//  document.getElementById("wynik").innerHTML = wynik; i++;   
// }


// do {
//    document.getElementById("wynik").innerHTML = wynik;
//    i++; 
// } while (i < 10)

int i = 0;
while (i < 5) {
  System.out.println(i);
  i++;
}