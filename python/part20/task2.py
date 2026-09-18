a = int(input('first num:-'))
b = int(input('second num:-'))
c = int(input('third num:-'))

if a> b and a> c:
    print('largest number is:,a')
elif b>c:
    print('largest number is:,b')
elif a == b and b == c:
    print('all are equels')    
else:
    print('largest number is:,c')        