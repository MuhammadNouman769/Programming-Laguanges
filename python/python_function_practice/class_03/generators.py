""" ==================== generators ===================== """

def my_gen():
    yield 100
    yield 200
    yield 300
    yield 400

gens = my_gen()

print(next(gens))
print(next(gens))
print(next(gens))
print(next(gens))


def count():
    for i in range(1, 6):
        yield i

gens = count()
for num in gens:
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
