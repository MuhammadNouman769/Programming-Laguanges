
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
