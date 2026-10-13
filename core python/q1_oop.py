'''
**Q: What is the difference between class attributes and instance attributes?**

Class attributes class ke andar define hote hain aur objects ke darmiyan shared hote hain. 
Instance attributes har object ki apni separate values rakhte hain.

`self` current object ko refer karta hai, aur `__init__` method object initialize karte waqt uski initial values set karta hai.
'''


class Student:
    school = "Punjab School" # class Atribute

    def __init__(self, name, marks):
        self.name = name # instance Atribute
        self.marks = marks # instance Atribute

student1 = Student("Nouman", 85)
student2 = Student("Ali", 72)
print(student1.name, student1.marks)
print(student2.name, student2.marks)
print(Student.school)
print(student1.school, student2.school)