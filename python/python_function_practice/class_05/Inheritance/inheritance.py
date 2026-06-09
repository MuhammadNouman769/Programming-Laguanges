

""" ================== Inheritance ================ """
'''
i. What is Inheritance?
answer: Inheritance OOP ka aik concept hai jisme ek class
        doosri class ki properties aur methods use krti hai
        
ii. Why do we use Inheritance?
answer: Inheritance code reusability ke liye use hoti hai.Is
        se hum parent class ka code dobara likhne ke bajaye 
        child class mein reuse kar sakte hain aur code 
        duplication kam hoti hai.


iii. what is parent class?
answer: parent class wo class hoti hai jis k method or 
        attributes dusri class use krti hai

iv. what is child class?
answer: jo class parent class se inherit krti hai or parent
        class k methods or attributes use krti hai wo child
        class hoti hai

v. what is super()?
Answer: super() parent class ke methods ya constructor ko 
        child class se call karne ke liye use hota hai.

vi. Q: What is Method Overriding?
Answer: jb child class parent class k methods ko same name se redefine kre

Example: 1
'''
class Animal:
    def eat(self):
        print('Animal is eating')
class Dog(Animal):
        def bark(self):
                super().eat()
d1 = Dog()
d1.bark()

'''
Example: 2
'''

class Person:
        def walk(self):
                print('walking')
class Student(Person):
        def walk(self):
                super().walk()
s1 = Student()
s1.walk()

'''
Example: 3
'''

class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    def start(self):
        super().start()
c1 = Car()
c1.start()

'''
Example: 4
'''
class Person:
        def speak(self):
                print('person is speaking')
class Student(Person):
        def speak(self):
                super().speak()
s1 = Student()
s1.speak()

''' ============== constructor in inheritance ================== '''
'''
Example: 1
'''
class Person:
        def __init__(self, name):
                self.name = name

class Student(Person):
        def __init__(self, name):
                super().__init__(name)


s1 = Student('Nouman')
print(s1.name)

'''
Example: 2
'''

class Employee:
        def __init__(self, name):
                self.name = name

class Manager(Employee):

        def __init__(self, name):
                super().__init__(name)

m1 = Manager('Ali')
print(m1.name)