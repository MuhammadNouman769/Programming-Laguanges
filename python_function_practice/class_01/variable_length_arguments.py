
""" ================= Variable-Length Arguments ================= """

def add(*args):
    print(sum(args))
add(1,2,3,4,5)

def employees(*args):
    print(args)
employees(2,4,4,5)

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
        print(total)
add(1,2,3,4,5)

def marks(*scores):
    total = 0
    for score in scores:
        total += score
        print(total)
marks(80,90,70,85)

def names(*students):
    print(" ".join(students))
names("Ali", "Nouman", "Ahmad")

def total(*numbers):
    total = 0
    for n in numbers:
        total += n
        print(total)

total(10, 20, 30, 40)