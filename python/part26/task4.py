
def addition(*args):
    num = 0
    for i in args:
        num = num + i
    return num    
print(addition(1,2,3,4,4,5,6,7))            

def info(**kwargs):
    return kwargs
print(info(name = 'daina', age=24, profession='Backend Enginner'))
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

