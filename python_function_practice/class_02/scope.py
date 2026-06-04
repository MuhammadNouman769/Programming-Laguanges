

""" =================== Scopes ================= """
def add(a, b):
    return a + b
print(add(1, 2))

# local scope

def func():
    x = 50
    print(x)
func()

# global scope

y = 30
def function():
    print(y)
function()

# modify global variable
x = 200
def function():
    global x
    x = 100
    print(x)
function()