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
# for i in range(n, 0,-1):
#     print(i)
s = 0
n = int(input("Enter number:-"))

for i in range(1, n+1):
    s = s + i
print(s)