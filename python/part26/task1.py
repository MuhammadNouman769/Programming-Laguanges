
def extragreeting(func):
    def msg():
        print('hi how r u')
        func()
        print('thankyou visit again')

    return msg

    

@extragreeting
def greetings():
    print('good morning')

                   
greetings()
