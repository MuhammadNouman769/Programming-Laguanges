class Factory:
    name = 'Toyota' # public class attribute
    _age = 12
    def __init__(self,type,tyre,color):
        self.type = type # public object attribute
        self.tyre = tyre
        self.color = color

obj = Factory('sudan', 'MRF', 'black')
print(obj.name)

obj.name = 'Honda city'
print(obj.name)
