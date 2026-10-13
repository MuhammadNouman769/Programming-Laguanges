'''
**Q1. What is `__str__` in Python?**

`__str__` ek special method hai jo object ki human-readable 
string representation return karta hai. Ye `print()` aur 
`str()` ke waqt use hota hai.

**Q2. What is `__repr__` in Python?**

`__repr__` object ki developer-friendly representation return karta hai. 
Ye debugging aur development ke liye useful hota hai. 
Ideally, representation itni clear honi chahiye ke object 
ki important details samajh aa saken aur mumkin ho to object ko dobara create bhi kiya ja sake.

**Q3. What is the difference between `__str__` and `__repr__`?**

`__str__` user-friendly output ke liye hota hai, jabke `__repr__` 
developer-friendly representation ke liye hota hai. 
Agar `__str__` define na ho aur `__repr__` available ho, 
to Python `__repr__` ko fallback ke taur par use kar sakta hai.
'''




class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"{self.name} works as a {self.role}"

    def __repr__(self):
        return f"Employee(name={self.name!r}, role={self.role!r}, salary={self.salary!r})"

emp1 = Employee('Nouman','Python Developer', 80000)
emp2 = Employee('Ali','Backend Developer', 60000)        

print(str(emp1))  # Output: Nouman works as a Python Developer
print(repr(emp1)) # Output: Employee(name='Nouman', role='Python Developer', salary=80000)
print(repr(emp2)) # Output: Employee(name='Ali', role='Backend Developer', salary=60000)
employee = Employee('Nouman', 'Python Developer', 80000)
print([employee])