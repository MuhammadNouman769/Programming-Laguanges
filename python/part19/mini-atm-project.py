
# Phir Mini Project #1

# Ye teen tasks complete hone ke baad:

# 🏧 Mini Project — ATM System

# Program mein:

# PIN login
# Maximum 3 attempts
# Successful login ke baad menu:
# ===== ATM =====
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

while True:

    balance = 10000

    print('========= Welcome To ATM ===========')

    choice = int(input("""
        1. press 1 to enter pin
        2. press 2 to check balance
        3. press 3 to cash deposit
        4. press 4 to cash withdraw
        5. press 5 to exit
        Enter your Choice:-
        """))


    if choice == 1:
        pin = (input('Enter pin'))
        if pin == '1234':
            print('login successfully!')
        else:
            print('invalid pin')
    elif choice == 2:           
        print(f'Amount is : {balance} ') 
    elif choice == 3:
        cash = int(input('Enter Amount deposit:-'))
        balance = balance + cash 
        print(f'Total Amount is :{balance}') 
    elif choice == 4:
        with_draw = int(input('Enter Amount:-'))
        if with_draw < balance:    
            print(f"cash withdraw successfult:{with_draw}")
            print(f"remianing balance:{with_draw - balance}")
        else:
            print('infsuficient balance') 
    elif choice == 5:
        print(' goodbuy ')
        
    else:
        print('invalid pin')    