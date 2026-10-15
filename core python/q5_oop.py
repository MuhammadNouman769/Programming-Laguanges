
'''
**Q1. What is operator overloading?**

Operator overloading mein hum special methods define 
karke operators ka behavior custom objects ke liye 
specify karte hain. For example, `__add__()` `+` operator ko implement karta hai.

**Q2. What is the difference between `__eq__` and `__lt__`?**

`__eq__` equality check karta hai aur `==` operator ke 
saath use hota hai. `__lt__` less-than comparison karta 
hai aur `<` operator ke saath use hota hai.

**Q3. What is the purpose of `__mul__`?**

`__mul__` `*` operator ka behavior define karta hai. 
Custom class is method ke zariye multiplication ko support kar sakti hai.

**Q4: What is `__hash__` in Python?**

`__hash__` object ka integer hash value return karta hai. 
Hashable objects ko sets aur dictionary keys mein use kiya ja 
sakta hai. Agar do objects equal hon, to unka hash equal hona 
zaroori hai. Lekin equal hash values ka matlab ye nahi ke objects lazmi equal hon.

2. Common operator special methods

Operator          	Special method
a + b           	__add__
a - b	            __sub__
a * b	            __mul__
a == b	            __eq__
a < b	            __lt__


'''
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __str__(self):
        return f"${self.amount}"

m1 = Money(500)
m2 = Money(200)

print((m1 + m2).amount)  # $700
print((m1 - m2).amount)  # $300
print((m1 * 2).amount)   # $1000
print(m1 == m2)          # False
print(m1 < m2)           # False
print(m1)                  # $500


class Amount:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount    

    def __lt__(self, other):
        return self.amount < other.amount

    def __hash__(self):
        return hash(self.amount)

m1 = Amount(500)
m2 = Amount(500)    
m3 = Amount(500)

print(m1 == m2)  # True
print(m1 < m2)   # False
print(hash(m1) == hash(m2))  # True
print(len({m1, m2, m3}))  # 2