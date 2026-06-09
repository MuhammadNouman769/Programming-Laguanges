

""" ================= Singale Inheritance ================ """

'''
1. what is single inheritance
Answer: jb aik child class siraf aik parent class se inherite kre

Example.i
'''
class Animal:
    def eat(self):
        print('Eating')

class Dog(Animal):
    def eat(self):
        super().eat()

d1 = Dog()
d1.eat()
