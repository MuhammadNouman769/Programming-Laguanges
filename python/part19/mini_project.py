"""Mini project: a PIN-protected ATM migrated from the original lesson."""

def deposit(balance, amount):
    """Return balance after a valid deposit."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    return balance + amount

def withdraw(balance, amount):
    """Return balance after a valid withdrawal."""
    if not 0 <= amount <= balance:
        raise ValueError("withdrawal is not available")
    return balance - amount

def main():
    balance = 10000.0
    authenticated = False
    for _ in range(3):
        if input("Enter PIN: ") == "1234":
            authenticated = True
            break
        print("Invalid PIN")
    if not authenticated:
        print("Too many attempts")
        return
    while True:
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            print(f"Balance: {balance}")
        elif choice == "2":
            balance = deposit(balance, float(input("Deposit: ")))
            print(f"Balance: {balance}")
        elif choice == "3":
            try:
                balance = withdraw(balance, float(input("Withdraw: ")))
                print(f"Balance: {balance}")
            except ValueError as error:
                print(error)
        elif choice == "4":
            print("Goodbye")
            return
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
