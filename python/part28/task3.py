
class Car:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f"Car(brand={self.brand}, model={self.model})"

    def __len__(self):
        return len(self.brand) + len(self.model)

    def __getitem__(self, index):
        if index == 0:
            return self.brand
        elif index == 1:
            return self.model
        else:
            return 'invalid index' 

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model     

    def __lt__(self, other):
        return self.price < other.price 

    def __gt__(self, other):
        return self.price > other.price
    

car1 = Car("Toyota", "Corolla", 50000)
car2 = Car("Toyota", "Corolla", 70000)
car3 = Car("honda", "city", 60000)

print(car1 == car2)

print(car1)

print(car1.brand)

print(car1.model)

print(repr(car1))

print(len(car1.brand))

print(len(car1.model))

print(len(car1))

print(car1[0])

print(car1[1])

print(car1[2])
print(car1 == car2)

print(car1 == car3)
print(car1 < car2)

print(car1 > car2)

 
car1.price = -50000
print(car1.price)
