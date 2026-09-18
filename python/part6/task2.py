"""Practice extending a parent class."""


class Account:
    def __init__(self, owner):
        self.owner = owner


class SavingsAccount(Account):
    def summary(self):
        return f"Savings account for {self.owner}"


def main():
    print(SavingsAccount("Amina").summary())


if __name__ == "__main__":
    main()
