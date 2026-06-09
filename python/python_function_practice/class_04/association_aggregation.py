

""" ======================== Association ======================= """

class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

t1 = Teacher("Usama")
s1 = Student("Nouman", t1)
print(s1.name)
print(s1.teacher.name)

class Teachers:

    def __init__(self, name):
        self.name = name

class Students:
    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers

t1 = Teachers("Usama Bhai")
s1 = Students("Nouman", t1)

print(s1.teachers.name)


class Engine:

    def __init__(self, name, egine_type,):
        self.name = name
        self.engine_type = egine_type

class Train:

    def __init__(self, name, rouite, speed, engine):
        self.name = name
        self.rouit = rouite
        self.speed = speed
        self.engine = engine

engine = Engine("GUC 20", "Locomotive")
train = Train("Ghouri Express", "Faisalabad to Lahore", "120 kilometers", engine)
print(train.name) # Ghouri express
print(train.engine.engine_type) # Locomotive
print(train.engine.name)
print(train.rouit) # Faisalabad to Lahore




class Driver:

    def __init__(self, name):
        self.name = name


class Bus:

    def __init__(self, driver):
        self.driver = driver


d1 = Driver("Ali")

b1 = Bus(d1)

print(b1.driver.name)



class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

t1 = Teacher("Usama","mathematics")
s1 = School("Govt High School", t1)
print(s1.teacher.subject) # mathematics


class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

a1 = Author("Noman")
b1 = Book("Python", a1 )
print(f' {b1.title} crash chourse by {b1.author.name}')
print(b1.author.name)