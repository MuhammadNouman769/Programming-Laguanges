
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = []

for row in matrix:
    for num in row:
        result.append(num)
print(result)

res =  [num for row in matrix for num in row]
print(res)