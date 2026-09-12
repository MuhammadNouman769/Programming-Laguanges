
""" ================ Diamond Problem ============== """
'''
1. Diamond problem kia hai 
 
diamond problem shape
                         A
                        / \
                       B   C
                        \ /
                         D

Answer: Diamond Problem multiple inheritance main tb hota
        hai jab aik class do aisi classes se inherit kare
        jo dono common class se inherit karti, is se method
        resolution mein ambiguity (confusion) paida hota hai.
Example:
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
d1.show()        
print(D.mro())

