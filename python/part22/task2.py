import random

computer = random.randint(1,100)
count = 1
number = int(input('guess the number:-'))
while number != computer:
    if number < computer:
        print('try higher')
    else:
        print('try lower')    

    number = int(input('guess the number:-'))
    count +=1
    if  count ==4:
        print('you have only one chance')
    elif count ==5:
        print('you are lose try again')
        break
    else:
        print('great you are the lucky')
else:
    print('correct guess in ',count,'attempts')