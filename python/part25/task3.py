
class Aminal:
    name = 'lion'

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'my name is {self.name}'    


obj1 = Aminal('lion')

print(obj1)        