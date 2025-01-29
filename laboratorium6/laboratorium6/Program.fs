open System
open System.Text.RegularExpressions


let str1 = "witaj w f#"
let str2 = " F#"

//let str3 = str1 + " w " + str2

//printfn "%s" str3

// split
let words = str1.Split([|','; ':'; ' '|], System.StringSplitOptions.RemoveEmptyEntries);
printfn "%A" words

let joined = String.Join(" - ", words)
printfn "%s" joined

printfn "%s" (str1.ToUpper())

let regex = Regex(@"\d+") // to znaczy dowolana cyfra od 0 - 9, + oznacza ze co najmniej jedno wystapienie

let isMatch = regex.IsMatch("test") // sprawdza czy w teksie jest conajmniej jedna liczba
printfn "%b" isMatch

let multiline = @"to jest 
wielo wierszowy 
tekst.
fadfa d
fdadfa
fafas
fdafa"

printfn "%s" multiline

open System.IO

let filePath = "output.txt"
let text = "to jest przykladowy tekst"

File.WriteAllText(filePath, text)

let lines = ["Linia 1"; "Linia 2"; "Linia 3"]
File.WriteAllLines(filePath, lines)

let text2 = "dodakowy tekst"
File.AppendAllText(filePath, text2)
File.AppendAllLines(filePath, lines)

let readtxt = File.ReadAllText(filePath)

printfn "Zawartosc pliku: %s" readtxt 


//Zadanie 1. Liczba słów i znaków
//Napisz program, który pobiera tekst od użytkownika, a następnie oblicza i wyświetla:
//• Liczbę słów w podanym tekście.
//• Liczbę znaków (bez spacji).


//licznie slow
let countWord (text: string) =
    text.Split([|' '; '\t'; '\n'; ';'; ':'; '.' |], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

//liczba zankow bez spacji
let countChar (text: string) =
    text.Replace(" ","").Length


//Zadanie 2. Sprawdzenie palindromu
//Stwórz funkcję, która sprawdza, czy podany ciąg znaków jest palindromem (czytany od przodu i od tyłu
//jest taki sam). Program powinien pobierać tekst od użytkownika i wyświetlać odpowiedni komunikat.


let checkIfPalindrom (text: string) =
    let clearText = text.Replace(" ","").ToLower()
    clearText = String(Array.rev(clearText.ToCharArray()))

[<EntryPoint>] // metoda uruchomieniowa jakby main, trzeba open System i 0 na koniec
let main argv =
    printf "Podaj tekst: " 
    let input = Console.ReadLine()
    let wordsCount = countWord input
    let charsCount = countChar input

    printfn "Liczba slow: %d" wordsCount
    printfn "Liczba zankow (bez spacja): %d" charsCount

    printf "Podaj tekst: " 
    let inputPalindrom = Console.ReadLine()

    if checkIfPalindrom inputPalindrom then
        printfn "Tesk jest palidoromem"
    else 
        printfn "nie jest palindromem"

    0


//Zadanie 3: Usuwanie duplikatów
//Napisz funkcję, która przyjmuje listę ciągów (np. słów) i zwraca nową listę, w której usunięte są
//duplikaty. Użytkownik powinien mieć możliwość wprowadzenia słów oddzielonych spacjami, a program
//powinien wyświetlić listę unikalnych słów

