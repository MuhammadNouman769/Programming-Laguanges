class Atm:

    # Constructor
    # __init__ automatically execute hota hai
    # jab object create hota hai.
    def __init__(self):
        self.pin = ""
        self.balance = 0
    def menu(self):
        while True:
            choice = input("""
            Hi, how may I help you?
            1. Press 1 to create PIN.
            2. Press 2 to change PIN.
            3. Press 3 to check balance.
            4. Press 4 to withdraw balance.
            5. Press anything else to exit.
            Enter your choice: 
            """)
            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.change_pin()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.withdraw()
            else:
                print("Thank you for using ATM!")
                break
    def create_pin(self):
        user_pin = input("Enter PIN: ")
        self.pin = user_pin
        user_balance = int(input("Enter balance: "))
        self.balance = user_balance
        print("PIN created successfully!")
    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid PIN!")
    def check_balance(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid PIN!")
    def withdraw(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Cash withdrawn successfully!")
                print("Remaining balance:", self.balance)
            else:
                print("Insufficient balance!")
        else:
            print("Invalid PIN!")
        self.menu()   

# Object creation
obj = Atm()
# Start ATM
obj.menu()