# Login program

email = input("Enter email: ")
password = input("Enter password: ")

if email == 'nomannisar769@gmail.com':

    if password == '@Usama22':
        print('User login successfully!')

    else:
        print('Incorrect password!')

        password = input('Enter password: ')

        if password == '@Usama22':
            print('Login successfully!')
        else:
            print('Incorrect password. You are blocked!')

else:
    print('Email invalid!')


