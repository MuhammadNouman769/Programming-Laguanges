def addition(*args):
    num = 0
    for i in args:
        num = num + i
    return num    
print(addition(1,2,3,4,4,5,6,7))            

def info(**kwargs):
    return kwargs
print(info(name = 'daina', age=24, profession='Backend Enginner'))
