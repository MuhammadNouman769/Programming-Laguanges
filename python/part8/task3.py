"""Practice factorial with a loop."""


def factorial(number):
    """Return a non-negative integer factorial."""
    result = 1
    value = 2
    while value <= number:
        result *= value
        value += 1
    return result


def main():
    print(factorial(int(input("Number: "))))


if __name__ == "__main__":
    main()
