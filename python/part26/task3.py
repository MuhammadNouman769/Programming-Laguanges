
def wrapper(func):
    def log():
        print('login success fully')
        func()
    
    return log

user_name = input('Enter username:-')
password  = input('Enter password:-')

@wrapper
def login():
    if user_name == 'nomannisar769' and password == '@Usama22':
        print('you are registered')
    else:
        print('try again!')    

login()