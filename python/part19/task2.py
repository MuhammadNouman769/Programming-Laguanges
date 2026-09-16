# Task 2 — ATM Login

# User se:

# Enter PIN:

# PIN ko check karo.

# Rules:

# Correct PIN → "Login successful!"
# Wrong PIN → dobara PIN maango
# Second attempt bhi wrong → "Account blocked!"

# Structure roughly aapke login program jaisi hogi:
while True:
        
    pin = input('Enter pin:-')
    if pin == '1234':
        print('login successfuly')
    elif pin != '1234':
        print('incorrect password try again')
        pin = input('Enter pin:-')
        if pin != '1234':
            print('Account blocked')
            break
        else:
            ('successfully login')
            
    else:
        print('try again')            

            
    