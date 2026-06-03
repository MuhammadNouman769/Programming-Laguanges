
""" ================ Positional Arguments ================== """


def student(name, math, science, english):
    print(f'{name} got {math}  {science} {english} marks')

student('Nouman', 80, 75, 90)

def car(brand, model, year):
    print(f'{brand} {model} {year}')

car(' Toyota', 'corolla', '2020')

def employ(name, salary, department):
    print(f'{name} earns {salary} in {department}')

employ('Ahmad', 50000, 'IT')


def order(item, quantity, price):
    print(f'{item} {quantity} costs {price}')
order('burger', '2x', 600)


def book(title, author, pages):
    print(f' {title} by {author} has {pages} pages')
book('python','john', 300)