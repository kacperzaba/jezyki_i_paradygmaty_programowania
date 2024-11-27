def inputValue(msg, start = 0, end = None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print("nieprawidolwe dane wejsciowe: ")
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print("Podano bledne dane")
            else:
                return int(inp) 

        else:
            return int(inp)
