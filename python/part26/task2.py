

class BagFactory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def detail(self):
        print('your bag detail')
        print(self.material)
        print(self.zips)
        print(self.pockets)

class Rebok(BagFactory):
    def __init__(self, material, zips, pockets, color):
        
        super().__init__(material, zips, pockets)
        self.color = color

    def details(self):

        # print('rebok detail')
        # print(self.material) 
        # print(self.zips)
        # print(self.pockets)
        print(self.color)
        return super().detail()

class Compus(Rebok):
    def __init__(self, material, zips, pockets, color, size ):
        super().__init__(material,zips,pockets,color)
        self.size = size

    def detail(self):
        print(self.size)
        return super().details()
        


obj1 = BagFactory('leather',3,2)
print(obj1.material)
obj1.detail()

obj2 = Rebok('recseen', 3, 1, 'blue')
obj2.details()

obj3 = Compus('polystor', 2, 3, 'red', 'large')
obj3.details()