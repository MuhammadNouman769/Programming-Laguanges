list1 = [1,2,3,[4,5,6,[7,8,9,[10,11,12,[13,14,15,[16,17,18]]]]]]
print(list1[3][3][3][3][3][-2])
print(list1[-2][-1])
a = 123
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a%10
    a = a//10
if copy == rev:
    print('palindrome number')
else:
    print('not a palindrome')     
