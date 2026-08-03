
# def hello(a,b):
#     print(a+b)


# hello(5,10 )



def palindrome_checker(number):
    copy = number
    rev = 0
    while number > 0:
        rev = rev * 10 + number % 10
        number = number // 10
    if copy == rev:
        print("this is palindrome")
    else:
        print("this is not palindrome")

palindrome_checker(121)           
palindrome_checker(123)
palindrome_checker(454)

# parameters and arguments
# parameters are the variables that are defined in the function definition,
# while arguments are the values that are passed to the function when it is called.

# position arguments 

def multiple(a,b,c):
    print(a*b*c)

multiple(2,3,4)
multiple(4,5,6 )

# default arguments

def multiply(a,b,c=2):
    print(a*b*c)

multiply(2,3)
multiply(2,3,4)

# keyword arguments

def divide(a, b):
    print(a / b)

divide(a=10, b=2)
divide(b=5, a=20  )