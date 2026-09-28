
class Car:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, value):
        if value < 0:
            print("Invalid price")
        else:
            self._price = value

car1 = Car(70000)            

print(car1.price)

car1.price = -5000
print(car1.price)