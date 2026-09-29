class Animal:
    a = 12
    def __init__(self,name):
        self.name = name # object/instance attritube

    def hello(self): #objeect/instatnce method
        print(f'how are you my name is {self.name}')

    @classmethod
    def details(cls): # class method        
        print(f'my name is {cls.a}')

    @staticmethod
    def speak():
        print('hello how are you')


obj = Animal("lion")

obj.hello()
obj.details()
obj.speak()