def numbers():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

num = numbers()
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

