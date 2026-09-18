"""Practice factorial with a loop."""


def factorial(number):
    """Return a non-negative integer factorial."""
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main():
    print(factorial(int(input("Number: "))))


if __name__ == "__main__":
    main()
