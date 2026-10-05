def my_decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()


def mydecorator(func):

    def wrapper(*args, **kwargs):

        # print("Asalam u alaikum")

        func(*args, **kwargs)

        print("i hope you are doing well")

    return wrapper


@mydecorator
def greet(name):
    print(f"Hello {name}")


greet("Nouman")


from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function")

        result = func(*args, **kwargs)

        print("After function")

        return result

    return wrapper