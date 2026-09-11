# class Atm:
#     name = "alfalah"

# obj = Atm()
# obj1 = Atm()
# print(obj.name)
# id(obj)
# print(id(obj1))


class fraction:

     # parameterized constructor 
    def __init__(self, x,y):
        self.num = x 
        self.den = y
    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den

        return "{}/{}".format(new_num,new_den)

fr1 = fraction(3,4)
fr2 = fraction(5,4)

print (fr1 + fr2)