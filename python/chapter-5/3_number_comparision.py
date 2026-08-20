while True:
    # greater number between two number
    number1 = int(input("Enter Number"))
    number2 = int(input("Enter Number"))
    number3 = int(input("Enter Number"))

    if number1 > number2 and number1 > number3:
        print(f"Number: {number1} is greater than Number: {number2} and Number: {number3}")
    elif number1 == number2 and number1 == number3:
        print(f"Number: {number1} Number: {number2}  and Number: {number3} are equal")
    elif number2 == number3 and number2 > number1 and number3 > number1:
            print(f"Number: {number1} lessthan Number: {number2} and Number:{number3} are equal")
    elif number1 == number3 and number1 > number2 and number3 > number2:
                print(f"Number: {number1} and Number: {number3} are equals and greaterthan Number: {number2}")                    
    elif number1 == number2 and number1 > number3:
            print(f"Number: {number1} and Number: {number2} are equal and greaterthan from Number: {number3}")    
    elif number2 > number1 and number2 > number3:
        print(f"Number: {number2} is greater than Number: {number1} and number: {number3}")
    else:
        print(f"Number: {number3} is greater than Number: {number1} and Number:{number2}")

