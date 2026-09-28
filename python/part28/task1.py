

mark = int(input('Enter Markks: '))

grade = 'A' if mark >= 80 else 'B' if mark >= 60 else 'C' if mark >= 50 else 'fail'

print(grade)

age  = int(input('Enter age: '))

ag = 'Adult' if age >= 18 else 'minor'
print(ag)

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

greater = f'{num1} is greater' if num1 > num2 else f'{num2} is greater'
print(greater)

num = int(input("Enter number: "))

result = 'Even' if num % 2 == 0 else 'Odd'
print(result)

marks = int(input('Enter marks'))
res = 'Pass' if marks >= 50 else 'fail'
print(res)