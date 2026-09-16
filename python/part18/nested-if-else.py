
# login program and indentation
# email -> nomannisar769@gmail.com
# password -> @Usama22
# login program and indentation

email = input("Enter email: ")
password = input("Enter password: ")

if email == 'nomannisar769@gmail.com' and password == '@Usama22':
    print('user login successfully!')
elif email == 'nomannisar769@gmail.com' and password != '@Usama22':
    print('incorrect password!')
    password = input('Enter password')
    if password == '@Usama22':
        print('login successfully')
    else:
        print('incorrect password you blocked')    

else:
    print('invalid credentials')