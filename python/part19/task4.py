"""Practice ATM withdrawal conditions."""

def withdrawal(balance, amount):
    """Return the new balance or a rejection message."""
    if amount <= 0:
        return "invalid amount"
    if amount > balance:
        return "insufficient funds"
    return balance - amount

def main():
    print(withdrawal(float(input("Balance: ")), float(input("Amount: "))))

if __name__ == "__main__":
    main()
