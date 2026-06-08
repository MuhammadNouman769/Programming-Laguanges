
""" ================= OOP ============== """

# getter
class Student:
    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

s = Student()
print(s.get_marks())

class Student:
    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks


    def set_marks(self, marks):
        self.__marks = marks

s = Student()

s.set_marks(95)

print(s.get_marks())


class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        self.__balance = balance

account = Account(50000)

account.set_balance(10000)
print(account.get_balance())




class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

s1 = Student("Muhammad Nouman", 25)


print(s1.get_name())

s1.set_name("Usama")
print(s1.get_name())

class Employee:

    def __init__(self,):