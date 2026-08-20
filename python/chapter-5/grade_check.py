while True:
    grade = int(input(" Enter Your Number Check Grade:-"))

    if grade > 100:    
        print("wrong try again less that 100")    

    elif grade >= 90:
        print(" You got -> A+")
    elif grade >= 80:
        print("you got -> A")
    elif grade >= 70:
        print("You got -> B")        
    elif grade >= 60:
        print("you got -> C")
    elif grade >= 50:
        print("you got -> D")

    else:
        print("Fail")    
        
number = int(input(""))
if number > 100 or number < 1:
    print("try between 0 to 100")
else:
    ("you win")    