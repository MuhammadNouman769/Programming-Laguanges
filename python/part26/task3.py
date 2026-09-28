
def wrapper(func):
    def log():
        print('login success fully')
        func()
    
    return log

user_name = input('Enter username:-')
password  = input('Enter password:-')

@wrapper
def login():
    if user_name == 'nomannisar769' and password == '@Usama22':
        print('you are registered')
    else:
        print('try again!')    

login()

class Animal:
    def __init__(self,name):
        self.name = name

class Human:
    def __init__(self,id):
        self.id = id 

class Robots(Human,Animal):
    def __init__(self, id,name):

        Human.__init__(self,id)
        Animal.__init__(self,name)

    def detail(self):
        print(self.id)
        print(self.name)    

robo = Robots(12,'akash')

robo.detail()
