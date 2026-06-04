

""" ==================== Lambda Function Practice ===================== """

""" Map """
double = lambda x: x * 2
print(double(10))

add = lambda a, b: a + b
print(add(10, 20))


is_even = lambda x: x % 2 == 0
print(is_even(4))


largest = lambda a, b, c: max(a, b, c)
print(largest(1, 2, 3))

multiply = lambda a, b:a * b
print(multiply(5, 4))


cube = lambda x: x ** 3
print(cube(3))

full_name = lambda first, last: f'{first} {last}'
print(full_name('Muhammad', 'Nouman'))

def square(num):
    return num ** 2
numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))

def square(num):
    return num / 2
numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))


numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, numbers)
print(list(result))


numbers = [10, 20, 30]
result = map(lambda x: x * 2, numbers)
for r in result:
    print(r)
print(list(result))


numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 3, numbers)
print(list(result))

prices = [1000, 200, 300]

result = map(lambda x: x +10, prices)
print(list(result))

numbers = [2, 4, 6]

result = map(lambda x: x * 5, numbers)

print(list(result))


names = ["ali", "ahmed", "nouman"]
result = map(lambda x: x.upper(), names)
print(list(result))

names = ["ALI", "AHMAD", "NOUMAN"]
result = map(lambda x: x.lower(), names)
print(list(result))

""" Filter """

# get even
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

# odd
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 != 0, numbers)
print(list(result))

numbers = [10, 15, 20, 25, 30 ]
result = filter(lambda x: x > 20, numbers)
print(list(result))

names = ["Ali", "Ahmed", "Nouman", "Usman"]
result = filter(lambda x: len(x) > 5, names)
print(list(result))

prices = [100, 250, 50, 400, 150]
result = filter(lambda x: x >= 150, prices)
print(list(result))