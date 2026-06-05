""" ==================== generators ===================== """

def my_gen():
    yield 100
    yield 200
    yield 300
    yield 400

gen = my_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def count():
    for i in range(1, 6):
        yield i

gen = count()
for num in gen:
    print(num)

def numbers():
    for i in range(10):
        yield i

n = numbers()
for num in n:
    print(num)


def gen():
    yield 10
    yield 20

g = gen()

print(next(g))
print(next(g))


def gen():
    for i in range(3):
        yield i

for x in gen():
    print(x)


def gen():
    yield 1
    yield 2
    yield 3

g = gen()

print(list(g))
print(list(g))
