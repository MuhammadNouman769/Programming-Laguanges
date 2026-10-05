

def my_decorator(func):

    def wrapper(*args, **kwargs):

        print("Calculating...")

        result = func(*args, **kwargs)

        print("Done!")

        return result

    return wrapper

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

@my_decorator
def add(a, b):
    return a + b


result = add(num1, num2)

print(result)