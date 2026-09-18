"""Practice a lambda expression."""


def square(number):
    """Return number squared using a lambda."""
    operation = lambda value: value * value
    return operation(number)


def main():
    print(square(int(input("Number: "))))


if __name__ == "__main__":
    main()
