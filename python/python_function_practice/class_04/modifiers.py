
""" ============== Access Modifiers ============== """

# public modifiers

class Student:
    def __init__(self, name, age):
        self.name = name      # Public
        self.age = age        # Public

s = Student("Nouman", 25)

print(s.name)
print(s.age)

# protected modifier

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

s = Student("Nouman", 25)
print(s._name)
print(s._age)

# private modifiers


class Student:
    def show_name(self, name, age):
        self.__name = name
        self.__age = age

s = Student("Nouman", 25)
obj = Student(s)

s.obj.show_name()















