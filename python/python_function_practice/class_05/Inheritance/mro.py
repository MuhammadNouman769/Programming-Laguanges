

""" ================= MRO (Method Resolution Order) ================== """
'''
1. What is MRO?

Answer: MRO define karta hai ke Python pehle kis class ka 
        method call karega jab multiple classes mein same 
        method exist ho.
Example.i
'''

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    def show(self):
        print("D")
d1 = D()
print(D.mro())

