while True:
    year = int(input("Enter year:-"))
    if year % 400 ==0:
        print("Leap Year")
    elif year % 100 == 0:
        print("not a leap year")
    elif year % 4 ==0:
        print("leap year")
    else:
        print("Not a Leap year")    

