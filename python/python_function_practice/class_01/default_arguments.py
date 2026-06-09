

""" ============== Default Arguments ==============="""

def student(name, age, city="Lahore"):
    print(f'{name} is {age} years old lives in {city}')

student(name="Nouman", age=27, city="Farooqabad")

def mobile(brand, price=50000):
    print(f'{brand} is {price} dollars')
mobile(brand="Samsung")

def book(title, pages=300):
    print(f'{title} is {pages} pages')
book(title="python")

def car(brand, model="COROLA", year=2020):
    print(brand, model, year)
car(brand="Toyota")

def mu_song(name, age=7):
    print(f'{name} is {age} months old')
mu_song(name="Usama")