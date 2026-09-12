# # class Atm:
# #     name = "alfalah"

# # obj = Atm()
# # obj1 = Atm()
# # print(obj.name)
# # id(obj)
# # print(id(obj1))


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

fr3 = fraction(3,4)
fr4 = fraction(5,4)



class Fraction:

    def __init__(self, x,y):
        self.numerator = x
        self.denumetor = y

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denumetor)

    def __add__(self,other):
        new_num = self.numerator*other.denumetor +other.numerator*self.denumetor
        new_den = self.denumetor*other.denumetor
        return "{}/{}".format(new_num,new_den)



fr1 = Fraction(5,1)
fr2 = Fraction(2,3)

print(fr1 + fr2)
