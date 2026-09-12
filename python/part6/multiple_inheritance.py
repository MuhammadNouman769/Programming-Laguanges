
""" ================= Multiple Inheritance =================== """
'''
1.what is Muptiple Inheritance
Answer: Jab ek child class 2 ya zyada parent classes se inherit kare.
'''

class Father:
    def skill(self):
        print('driving')

class Mother:
    def skill2(self):
        print('cooking')

class Child(Father, Mother):
    def both(self):
        super().skill()
        super().skill2()

c1 = Child()
c1.both()