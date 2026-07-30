# while True:
#     number = int(input("Enter a Number:-"))
#     if number == 0:
#         number = 1
#     for index, i in enumerate(range(number, (number*10) + 1, number)):
#         print(f" {number} x {index} = {i}")   

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# n = int(input("Enter number:-"))
# # for i in range(n, 0,-1):
#     print(i)
# s = 1
# n = int(input("Enter number:-"))

# for i in range(1, n+1):
#     s = s * i
# print(s)

# oddsum = 0
# evensum = 0

# number = int(input("Enter your number:-"))

# for i in range(number):
#     if i %2 == 0:
#         oddsum = oddsum + 1
#     else:
#         evensum = evensum + 1
# print(f" odd sum number is {oddsum} eve sum number {evensum}")        

# n = int(input("Enter number:-"))
# s = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         s = s +1 
# if s == 2:
#     print("prime")
# else:
#     print("composite")

# a = "python"
# for i in range(len(a)-1,-1,-1):
#     print(i)

# from string import digits


# from curses.ascii import isalpha, isdigit


# a = "34grfy54@!%g5684greg59467rgh954ghbn467hb5473b"

# char = 0
# spchar = 0
# digits  = 0

# for i in a:
#     if i.isdigit():
#         digits = digits + 1
#     elif i.isalpha():
#         char = char + 1
#     else:
#         spchar = spchar + 1
# print(f" characters = {char}, special characters = {spchar}, digits = {digits}")                

a = "34grfy54@!%g5684greg59467rgh954ghbn467hb5473b"

char = 0
spchar = 0
digits  = 0

for i in a:
    if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        char += 1
    elif  ord(i) >= 48 and ord(i) <= 57:
        digits += 1
    else:
        spchar += 1
print(f" characters = {char}, special characters = {spchar}, digits = {digits}")                

a = "34grfy54@!%g5684greg59467rgh954ghbn467hb5473b"

char = 0
digits = 0
spchar = 0

char_list = []
digit_list = []
spchar_list = []

for i in a:
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        char += 1
        char_list.append(i)

    elif 48 <= ord(i) <= 57:
        digits += 1
        digit_list.append(i)

    else:
        spchar += 1
        spchar_list.append(i)

print("Characters =", char, char_list)
print("Digits =", digits, digit_list)
print("Special Characters =", spchar, spchar_list)