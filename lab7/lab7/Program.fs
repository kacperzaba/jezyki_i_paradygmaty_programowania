open System

type Osoba(imie: string, wiek: int) =
    member this.Imie = imie
    member this.Wiek = wiek

    member this.Info() = printfn "Witaj %s, masz %d lat" this.Imie this.Wiek

//obiekt 
let osoba1 = Osoba("Jan", 18)
osoba1.Info()

//type Osoba1() =
//    val mutable Imie: string 
//    val mutable Wiek: int

//    //konctrukor
//    new(imie, wiek) = {Imie = imie; Wiek = wiek}
//    new() = Osoba1("brak", 0)

type Student(imie: string, wiek: int, nrAlbumu: int) =
    inherit Osoba(imie, wiek) //dziedziczenie
    member this.NrAlbumu = nrAlbumu

let student = Student("Pioczrus", 30, 68299)

[<AbstractClass>]
type Figura() =
    abstract Pole: unit -> float
    abstract Obwod: unit -> float

type Kolo(promien: float) =
    inherit Figura()
    override this.Pole(): float = Math.PI * promien * promien
    override this.Obwod (): float = 2.0 * Math.PI * promien 

let kolo = Kolo(5.0)
printfn "Pole kola %.2f" (kolo.Pole())
printfn "Obowod kola %.2f" (kolo.Obwod())

type IFigura =
    abstract Opis: unit -> unit

type kwadrat() =
    interface IFigura with
        member this.Opis() = printfn "To jest kwadrat"

let kw = kwadrat() :> IFigura //definiujemyu obiekt kwadrat i go rzutujemy na interface
kw.Opis()

//Zadanie 1. System do zarządzania biblioteką
//Zaproponuj system do zarządzania biblioteką, który będzie zwierał klasy do reprezentowania książek,
//użytkowników biblioteki oraz samej biblioteki, z funkcjonalnością do dodawania i usuwania książek oraz
//wypożyczania ich użytkownikom. Program powinien zawierać:
//• Klasa Book: Reprezentuje książkę z tytułem, autorem i liczbą stron. Posiada metodę GetInfo()
//zwracającą informacje o książce.
//• Klasa User: Reprezentuje użytkownika biblioteki, który może wypożyczać i zwracać książki.
//Posiada metody do wypożyczania (BorrowBook) oraz zwracania (ReturnBook) książek.
//• Klasa Library: Reprezentuje bibliotekę, która zarządza kolekcją książek. Posiada metody do
//dodawania (AddBook), usuwania (RemoveBook) oraz listowania (ListBooks) książek.
//• Program główny: Tworzy instancję biblioteki i użytkownika, dodaje książki do biblioteki,
//wypożycza i zwraca książki przez użytkownika oraz wyświetla aktualny stan biblioteki.

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    member this.GetInfo = printfn "Tytuł: %s, autor: %s, ilośc stron: %d" this.Title this.Author this.Pages

type User(name: string) =
    let mutable borrowedBooks = []
    member this.Name = name
    member this.BorrowBook(book: Book) = 
        book :: borrowedBooks 
        printfn "Uzytkownik %s wypozyczyl ksiazka: %A" this.Name book.Title

    member this.ReturnBook(book: Book) =
        
