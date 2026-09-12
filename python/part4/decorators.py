
"""  =========================== decorators ======================== """

def my_decorator(func):

    def wrapper():
        print('start')

        func()

        print('end')
    return wrapper


@my_decorator
def my_func():
    print('hello world')
my_func()


