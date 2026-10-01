

def even_squares(numbers):

    for number in numbers:

        if number % 2 == 0:

            yield number ** 2

numbers = range(1, 11)
result = even_squares(numbers)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
