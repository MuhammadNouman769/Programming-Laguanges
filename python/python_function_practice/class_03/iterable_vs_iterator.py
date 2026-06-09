""" ===================== iterable vs iterator ====================="""

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    print(n)


iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

name = "Nouman"

iterator = iter(name)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


number = [5, 10,2]

it = iter(number)

print(next(it))
print(next(it))
print(next(it))

numbers = [100, 200, 300]

it = iter(numbers)

print(next(it))
print(list(it))