# polimaphisam


class Animal:
    a = 12
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f'your name is {self.name}')

class Human(Animal):
    b = 12
    # def __init__(self, name):
    #     super().__init__(name)            

    def info(self):
        print(f'your info is {self.name} and this is all we have')        

obj = Human('Nouman')

print(obj.a)
print(obj.b)

obj.details()
obj.info()

