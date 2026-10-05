

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

even = [num for row in matrix for num in row if num % 2 == 0]
print(even)

def add(num):
    return  num + num

numbers = [1, 2, 3, 4]
result = [add(num) for num in numbers]
print(result)