start = [1, 3, 0, 5, 8, 5]
koniec = [2, 4, 6, 7, 9, 9]

i = 0
print(i, end=" ")

for j in range(len(koniec)):
    if start[j] >= koniec[i]:
        print(j, end=" ")
        i = j