'''**Q1. What is inheritance in Python?**

Inheritance ek OOP concept hai jisme child class parent class ke
attributes aur methods ko reuse aur extend kar sakti hai. Is se 
code duplication kam hoti hai. Python mein `super()` parent class 
ke methods, jaise `__init__`, call karne ke liye use hota hai.

**Q2. What is composition in Python?**

Composition ek OOP concept hai jisme ek class apne andar doosri class ka 
object rakhti hai aur uski functionality use karti hai. 
Ye has-a relationship represent karti hai, jaise Car has an Engine.

**Q3. What is the difference between inheritance and composition?**

Inheritance is-a relationship represent karti hai, 
jabke composition has-a relationship represent karti hai. 
Inheritance mein child class parent se behavior inherit karti hai, 
jabke composition mein ek object doosre object ko use karta hai. 
Composition zyada flexible design dene mein madad kar sakti hai.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(
            f"My name is {self.name} "
            f"and I am {self.age} years old."
        )


class Developer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def code(self):
        print(f"{self.name} writes code in {self.language}.")


class CPU:
    def process(self):
        print("CPU is processing data.")


class Laptop:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor
        self.cpu = CPU()  # Composition

    def run(self):
        print(f"{self.brand} laptop is starting.")
        print(f"Processor: {self.processor}")
        self.cpu.process()


dev1 = Developer("Nouman", 25, "Python")
dev1.introduce()
dev1.code()

laptop1 = Laptop("Dell", "Intel Core i5")
laptop1.run()
