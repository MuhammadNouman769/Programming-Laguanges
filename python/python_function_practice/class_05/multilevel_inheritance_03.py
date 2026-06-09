

""" ================ Multilevel Inheritance =============== """
'''
what is Multilevel Inheritance
Answer: Multi-level Inheritance me aik child class
        parent class se inherit karti hai,or parent
        grand parent class se inherit karti hai.

Example.1
'''
class GrandParent:

    def house(self):
        print('old house')

class Parent(GrandParent):
    def house(self):
        return super().house()

class Child(Parent):
    def house(self):
        super().house()

c1 = Child()
c1.house()