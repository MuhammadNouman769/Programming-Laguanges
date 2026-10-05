'''
  Variables kia hote hain?
 Variable aik named memory location hota hai jo data ko temporarily store karta hai.        
''' 
name = "John"  # String variable
age = 25  # Integer variable
list1 = [1, 2, 3, 4, 5]  # List variable
dict1 = {"name": "Alice", "age": 30}  # Dictionary variable
tuple1 = (10, 20, 30)  # Tuple variable

'''
Q6. What is mutable and immutable in python?
Mutable wo data types hote hain jin ki value change ki ja sakti hai.
Example: List, Dict, Set. Immutable wo data types hote hain jin ki value
change nahi ki ja sakti. Example: Tuple, String, Int.
'''

license_plate = "ABC123"  # Immutable string variable
license_plate = "ABC123V"  # Reassigning the variable to a new string (creates a new object)
print(license_plate)

number = [1, 2, 3]  # Mutable list variable
number[0] = 2
print(number)

'''
Q8. What is Type Casting in Python?
 Aik data type ko dusre data type me convert karna Type Casting kehlata hai.
Do types hoti hain: Implicit - Python automatically convert karta hai. Explicit -
Hum manually conversion karte hain.'''

a = 2
b =2.5
c = a+b
print(c)
a = 2
b =int(2.5)
c = a+b
print(c)
name = "John"
age = str(25)  # Explicit type casting from string to integer
print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>
'''

Q11. Difference between parameter and argument?
 Parameter wo variable hota hai jo function define karte waqt parentheses ke 
andar likha jata hai. Argument wo actual value hoti hai jo 
function call karte waqat pass ki jati hai.
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

student1 = Student("John", 25)  # Argument values passed to the constructor
print(student1)  # Output: John
print(student1.name)  # Output: John
print(student1.age)   # Output: 25

'''
Q12. Types of Arguments in Python?
 Positional Arguments,
 Keyword Arguments, 
 Default Arguments, 
 Variable-Length Arguments (*args, **kwargs).

1.
jaha order tarteeb matter krti hai
2.Keyword Arguments, 
Function call karte waqat parameter ka naam likh kar value pass ki jati hai. Example: student(name="Ali", age=22)
3. Default Arguments, 
jaha parameter ki value pehle se set hoti hai 
4. variable-length arguments
   
 
 '''

