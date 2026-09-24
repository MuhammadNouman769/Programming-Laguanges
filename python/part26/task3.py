

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