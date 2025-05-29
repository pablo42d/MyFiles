// Od tablic do obiektów
// Przykład obiektów w JavaScript, programista samodzielnie programuje klucze i wartości

const students = [
    { id: 1, name: "Jan", age: 20 },
    { id: 2, name: "Anna", age: 22 },
    { id: 3, name: "Piotr", age: 21 }
];
// Przykład obiektu z kluczami i wartościami
const student = {
    id: 1,
    name: "Jan",
    age: 20
};  

var hero = {
    name: "Superman",
    power: "Flight",
    strength: 100,
    abilities: ["X-ray vision", "Super speed", "Heat vision"],
    displayInfo: function() {
        console.log(`Hero: ${this.name}, Power: ${this.power}, Strength: ${this.strength}`);
    }
};  
// Wyświetlenie informacji o bohaterze
hero.displayInfo(); // Hero: Superman, Power: Flight, Strength: 100



// Dodanie nowej właściwości do obiektu metody obiektu
var dog = {
    name: "Rex",
    breed: "German Shepherd",
    age: 5,
    bark: function() {
        console.log(`${this.name} says Woof!`);
        alert(`${this.name} says Woof! Woof!`);
    },
    displayInfo: function() {
        console.log(`Dog Name: ${this.name}, Breed: ${this.breed}, Age: ${this.age}`);
    }
};
// Wywołanie metody bark
dog.bark(); // Rex says Woof!
// Wywołanie metody displayInfo
dog.displayInfo(); // Dog Name: Rex, Breed: German Shepherd, Age: 5

// Dostęp do właściwości obiektu
console.log(dog.name); // Rex
console.log(dog['bark']); // function() { console.log(`${this.name} says Woof!`); }

// Dane i obiekt w obiekcie
var book = {
    title: "JavaScript Basics",
    year: 2020,
    author: {
        name:"John",
        surname: "Doe"
    },
    
    displayInfo: function() {
        console.log(`Book Title: ${this.title}, Author: ${this.author}, Year: ${this.year}`);
    }
};
console.log(book.author.name);
console.log(book['author']['surname']); // Doe
console.log(book['author'].name); // John
console.log(book.author['name']); // John

// Porównanie obiektów
var person1 = {
    name: "Alice",
    age: 30
};
var person2 = {
    name: "Alice",
    age: 30
};  
console.log(person1 === person2); // false, ponieważ to różne obiekty w pamięci
console.log(JSON.stringify(person1) === JSON.stringify(person2)); // true, porównanie wartości obiektów 

var fido = { breed: "pies"};
var rex = { breed: "pies"};
// Porównanie obiektów z użyciem operatora porównania
console.log(fido === rex); // false, ponieważ to różne obiekty w pamięci


// Przypisanie referencji do obiektu
var mydog = rex; // przypisanie referencji do obiektu
// Porównanie obiektów z użyciem operatora porównania
console.log(fido === mydog); // false, ponieważ to różne obiekty w pamięci
// Porównanie obiektów z użyciem operatora porównania
console.log(rex === mydog); // true, ponieważ to ten sam obiekt w pamięci


// Porównanie obiektów z użyciem funkcji
function areObjectsEqual(obj1, obj2) {
    return JSON.stringify(obj1) === JSON.stringify(obj2);
}
console.log(areObjectsEqual(person1, person2)); // true, porównanie wartości obiektów
// Porównanie obiektów z różnymi właściwościami
var person3 = {
    name: "Alice",
    age: 30,
    city: "New York"
};
var person4 = {
    name: "Alice",
    age: 30
};
console.log(areObjectsEqual(person3, person4)); // false, różne właściwości

// Iteracja po obiekcie
for (var key in dog) {
    if (dog.hasOwnProperty(key)) {
        console.log(`${key}: ${dog[key]}`);
    }
}

// metody wywołujące

var hero2 = {
    name: "Batman",
    power: "Intelligence",
    occupation: "Detective",
    strength: 90,
    abilities: ["Martial arts", "Stealth", "Gadgets"],
    say: function() {
        return 'Moja specjalizacja to ' + hero2.occupation;
        // return 'Moja specjalizacja to ${this.name}, the Dark Knight!`;
        // this jest kontekstem obiektu, w którym jest wywoływana metoda
        // return this.name + ', the Dark Knight!';
    },
    displayInfo: function() {
        console.log(`Hero: ${this.name}, Power: ${this.power}, Strength: ${this.strength}`);
    }
};
console.log(hero2.say()); // Moja specjalizacja to Detective
console.log(hero2.say('a', 'b', 'c')); // Moja specjalizacja to Detective
console.log(hero2['say']()); // Moja specjalizacja to Detective
// console.log(hero2.say()); // Batman, the Dark Knight! (błąd, ponieważ nie ma takiej właściwości w obiekcie hero2)


// Konstruktor obiektu Duża litera H wskazywana jest jako konwencja, aby wskazać, że jest to konstruktor obiektu a nie funkcja
// Przykład konstruktora obiektu Hero
function Hero() {
    this.occupation = "Superhero";
}
var hero4 = new Hero();
console.log(hero4.occupation); // Superhero

// __________________________________________________________

function Hero1(name, power, strength, abilities) {
    this.name = name;
    this.power = power;
    this.strength = strength;
    this.abilities = abilities || [];
    this.displayInfo = function() {
        console.log(`Hero: ${this.name}, Power: ${this.power}, Strength: ${this.strength}`);
    };
}
// Tworzenie instancji obiektu Hero
var hero3 = new Hero1("Superman", "Flight", 100, ["Super strength", "X-ray vision"]);
hero3.displayInfo(); // Hero: Superman, Power: Flight, Strength: 100

// Można utworzyć wiele instancji obiektu Hero
function Hero2(name, power, strength, abilities) {
    this.name = name;
    this.power = power;
    this.strength = strength;
    this.abilities = abilities || [];
    this.whoAreyou = function() {
        return 'Jestem ' + this.name + ', mam moc ' + this.power + ' i siłę ' + this.strength;
    };
}


var h1 = new Hero2("Batman", "Intelligence", 90, ["Martial arts", "Stealth"]);
var h2 = new Hero2("Wonder Woman", "Super strength", 95, ["Combat skills", "Lasso of Truth"]);
console.log(h1.whoAreyou()); // Jestem Batman, mam moc Intelligence i siłę 90
console.log(h2.whoAreyou()); // Jestem Wonder Woman, mam moc Super strength i siłę 95
var h = Hero2("Flash", "Super speed", 85, ["Time travel", "Lightning bolt"]);
// h jest undefined, ponieważ nie użyto słowa kluczowego new
console.log(typeof h); // undefined
// Poprawne użycie konstruktora Hero2   
var h3 = new Hero2("Flash", "Super speed", 85, ["Time travel", "Lightning bolt"]);
console.log(h3.whoAreyou()); // Jestem Flash, mam moc Super speed i siłę 85


// __________________________________________________________
// Iteratory
// Iteracja next() zwraca obiekt z właściwościami value i done
function iter(array) {
    var nextIndex = 0;
    return {
        next: function() {
            if (nextIndex < array.length) {
                return { value: array[nextIndex++], done: false };
            } else {
                return { done: true };
            }
        }
    };
}
// Przykład użycia iteratora
var it = iter(["Witajcie", "Iteratory!!"]);
console.log(it.next()); // { value: 'Witajcie', done: false }
console.log(it.next().value); // { value: 'Iteratory!!', done: false }
console.log(it.next().done); // { done: true }



function createIterator(array) {
    let index = 0;
    return {
        next: function() {
            if (index < array.length) {
                return { value: array[index++], done: false };
            } else {
                return { done: true };
            }
        }
    };
}

// Przykład użycia iteratora
const myArray = [1, 2, 3, 4, 5];    
const myIterator = createIterator(myArray);
console.log(myIterator.next()); // { value: 1, done: false }

// Obiekty Iterowne
let iter1 = {
    0: "Witajcie",
    1: "Swiecie",
    2: "Iteratory!!",
    length: 3,
    [Symbol.iterator]:() => {
        // Funkcja zwracająca iterator
        let index = 0;
        return {
            next: () => {
                let value = this[index];
                let done = index >= this.length;
                index++;
                return { value, done };
            }
        };
    }
};
// Użycie iteratora
// iter1[Symbol.iterator] = function() {
//     let index = 0;
//     return {
//         next: () => {
//             if (index < this.length) {
//                 return { value: this[index++], done: false };
//             } else {
//                 return { done: true };
//             }
//         }
//     };
// };
for (let item of iter1) {
    console.log(item);
}

// Map jako obiekt iterowalny dopuszcza iterację po parach klucz-wartość
let myMap = new Map([
    ["name", "Alice"],
    ["age", 30],
    ["city", "New York"]
]);
console.log(myMap.get("name")); // Alice
console.log(myMap.get("age")); // 30

const obj = {}
    const m2 = new Map([
        ["name", "Alice"],
        ["age", 30],
        ["city", "New York"]
    ]);
console.log(m2.has(obj)); // false, ponieważ obj nie jest kluczem w mapie
console.log(m2.has("name")); // true, ponieważ "name" jest kluczem w mapie

// Metody set(key, value) i get(key) w Map można łączyć w łańcuch
const m3 = new Map().set("name", "Alice").set("age", 30).set("city", "New York");
console.log(m3.get("name")); // Alice
console.log(m3.get("age")); // 30
console.log(m3.get("city")); // New York

// Iteracja po mapie
for (let [key, value] of m3) {
    console.log(`${key}: ${value}`);
}
// name: Alice
// age: 30
// city: New York
for (let entry of m3.values()) {
    console.log(entry);
}

for (let key of m3.keys()) {
    console.log(key);
}


// Iteracja po mapie z użyciem forEach
m3.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// Metoda entries() zwraca iterator po parach klucz-wartość
const entriesIterator = m3.entries();
for (const entry of entriesIterator) {
    console.log(`${entry[0]}: ${entry[1]}`);
}

// Operator rozwijania (...) pozwala na łatwe tworzenie nowych map z istniejących
const m4 = new Map([...m3, ["country", "USA"]]);
console.log(m4.get("country")); // USA

// Metoda keys() zwraca iterator po kluczach mapy
// Można użyć operatora rozwijania (...) do utworzenia tablicy z kluczami
const m5 = new Map([
    [1, "one"],
    [2, "two"],
    [3, "three"]
]);
const keys = [...m5.keys()];
console.log(keys); // [1, 2, 3]
// można również użyć metody Array.from() do utworzenia tablicy z kluczami
const arr = [...m5];
console.log(arr); // [1, 2, 3]
// const arr = Array.from(m5.keys());
// console.log(arr); // [[1, "one"], [2, "two"], [3, "three"]]


// _________________________________________________________________________________

// SET

// Set może być dowolnego typu wartość musi być unikalna
const s = new Set();
s.add(1);
s.add(2);
s.has(1); // true
s.delete(1); // usuwa wartość 1
s.has(1); // false, ponieważ wartość 1 została usunięta
s.clear(); // usuwa wszystkie wartości
s.add(1);
s.add(2);

// zbiór za pomocą iteratora
const colors = new Set(["red", "green", "blue"]);

// weak map i weak set
// WeakMap i WeakSet przechowują referencje do obiektów, które mogą być garbage collected obsługuje metody takie jak set(), get(), has() i delete().
// WeakMap przechowuje pary klucz-wartość, gdzie klucze są obiektami, a wartości mogą być dowolnego typu. WeakSet przechowuje tylko obiekty.
// Weak Set obsługuje metody takie jak add(), has() i delete(). WeakMap i WeakSet nie są iterowalne, co oznacza, że nie można używać pętli for...of ani metod takich jak forEach().

// __________________________________________________________________________________
// Klasy i obiekty

// Klasy w JavaScript są szablonami do tworzenia obiektów, które mogą zawierać właściwości i metody.
// Klasy są definiowane za pomocą słowa kluczowego class, a ich instancje są tworzone za pomocą słowa kluczowego new.

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}
console.log(typeof Person); // function, ponieważ klasa jest funkcją

// Anonimowe wyrażenie klasy
const Animal = class {
    constructor(name, species) {
        this.name = name;
        this.species = species;
    }

    speak() {
        console.log(`${this.name} says hello!`);
    }
};


const NamedCar = class Car {
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }
}
getName(); {
    // Metoda zwracająca nazwę klasy
    // W przypadku anonimowej klasy, nazwa będzie undefined
    // W przypadku NamedCar, nazwa będzie Car
    // ponieważ klasa jest anonimowa, ale ma nazwę Car

    return Car.name;
}
const ford = new NamedCar();
console.log(ford.getName()); // Car, ponieważ klasa jest anonimowa
console.log(ford.name); // Car, ponieważ klasa jest anonimowa


class Truck {
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }
}   
const myTruck = new Truck("Ford", "F-150", 2022);
console.log(myTruck.make); // Ford
console.log(myTruck.model); // F-150
console.log(myTruck.year); // 2022
console.log(myTruck.make.model.year); // undefined, ponieważ make, model i year są właściwościami obiektu myTruck, a nie metodami

// Klasa z metodą statyczną
class Vehicle {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    static getVehicleType() {
        return "This is a vehicle.";
    }
}
// Wywołanie metody statycznej
console.log(Vehicle.getVehicleType()); // This is a vehicle.

// Klasa z metodą statyczną i właściwością statyczną
class Car {
    static type = "Car";

    constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    static getType() {
        return Car.type;
    }
}
// Wywołanie metody statycznej
console.log(Car.getType()); // Car

class Logger {
    static log(level, message) {
        console.log(`Log: ${level}: ${message}`);
    }
}
// Wywołanie metody statycznej
Logger.log("Warning", "This is a warning message."); // Log: Warning: This is a warning message.

// nie ma instancji klasy Logger, ponieważ jest to klasa statyczna
// const Logger = new Logger(); // TypeError: Logger is not a constructor
// Logger.log("Error", "This is an error message."); // TypeError: Logger.log is not a function

