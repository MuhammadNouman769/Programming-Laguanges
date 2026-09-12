

""" ===================== Hierarchical Inheritance ==================== """

'''
1.What is hierarchical inheritance
Answer: jab aik parent class se multiple child class inherit kare

Example.i
'''
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()

d.eat()
c.eat()