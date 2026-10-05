

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = [num ** 2 for num in numbers if num % 2 != 0]
print(odd)

number = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

unique_sq = {num ** 2 for num in number if num % 2 == 0}
print(unique_sq)

dict_numbers = [1, 2, 3, 4, 5, 6]

squ = {num:num ** 2 for num in dict_numbers if num % 2 == 0}

print(squ)