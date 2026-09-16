# Task 3 — Simple Calculator

# User se 2 numbers aur operator lo:

# Enter first number: 20
# Enter second number: 5
# Enter operator: /

# Support:

# + 
# -
# *
# /
while True:

    number1 = int(input('Enter number first:- '))
    number2 = int(input('Enter number second:- '))
    operator = input('Enter operator:- ')

    if operator == '+':
        print(f'Result: {number1 + number2}')
    elif operator == '-':
        print(f'Result: {number1 - number2}')
    elif operator == '*':
        print(f'Result: {number1 * number2}')
    elif operator == '/':
        print(f'Result: {number1 / number2}')
    elif operator == '0':
        print(' can not divide by zero')
    else:
        print('invalid')
