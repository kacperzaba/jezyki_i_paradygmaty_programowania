open System
open System.Collections

type LinkedList<'T> =
    | Empty
    | Node of 'T * LinkedList<'T>

let Head =
    function
    | Empty -> failwith "Nie mozna pobrac glowy - lista pusta." //failwith przerywa dzialanie programu i zglasza wynik
    | Node(Head, _) -> Head

let Tail =
    function
    | Empty -> failwith "Nie mozna pobrac ogona - lista pusta." //failwith przerywa dzialanie programu i zglasza wynik
    | Node(Tail, _) -> Tail

let addHead value list =
    Node(value, list)

let rec printList list =
    match list with
        | Empty -> ()
        | Node(value, next) -> 
            printf "%A " value 
            printList next

[<EntryPoint>]
let main argv =
    let list1 = Empty
    let list2 = addHead 1 list1
    let list3 = addHead 2 list2

    printList list1
    printList list2
    printList list3




    0