""" ===================== Recursion ===================== """

# normal function

def test():
    print("Hello World")

test()

# recursion

def test(n):
    if n == 0:
        return
    print(n)
    test(n - 1)

test(50)


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(4))