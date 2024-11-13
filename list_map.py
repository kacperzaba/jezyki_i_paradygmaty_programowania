from functools import reduce
from tkinter.scrolledtext import example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# listy skladane

numbers1 = [x ** 2 for x in numbers if x % 2 != 0]
print(numbers1)

def fun1(x):
    return x * x

# mapowanie - map
numbers2 = list(map(lambda x : x * 2, numbers)) # wazna jest konwersja na liste
numbers3 = list(map(fun1, numbers, ))
print(numbers2)
print(numbers3)

# filtrowanie elemetnow - filter
def fun2(x):
    return x % 2 == 0

numbers4 = list(filter(fun2, numbers))
numbers5 = list(filter(lambda x: x%2==0, numbers))

print(numbers4)
print(numbers5)

# zwracanie jednkego elemetntu z listy - reduce
numbers6 = reduce(lambda x, y: x + y, numbers)
print(numbers6)

numbers7 = reduce(lambda x, y: x if x > y else y, numbers)
print(numbers7)

# wykonywanie kodu ktory zostal przekazany jako lancuhc znakow - eval
b = 10
example = '2+2-1+b'
result = eval(example)
print(result)

# funkcja pozwalajacy na wykonywanie dynamiczne kodu (rowniez jako string)
code = """
for i in range(3):
    print("witaj ", i)
"""
exec(code)