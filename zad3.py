zadania = [
    # [zadanie, czas,nagorda],
    ['zad1', 3, 12],
    ['zad2', 1, 6],
    ['zad3', 8, 26],
    ['zad4', 10, 34],
    ['zad5', 1, 14]
]

zadania2 = zadania.copy()

czas_oczekiwania = 0
for i in range(len(zadania) - 1):
    if zadania[i][2] < zadania[i+1][2] or (zadania[i][2] == zadania[i+1][2] and zadania[i][1] > zadania[i+1][1]):
        zadania[i], zadania[i + 1] = zadania[i + 1], zadania[i]

for zad in zadania:
    czas_oczekiwania += zad[1]

print(zadania, czas_oczekiwania)

zadania2.sort(key=lambda x: (-x[2], x[1]))
print(zadania2, czas_oczekiwania)