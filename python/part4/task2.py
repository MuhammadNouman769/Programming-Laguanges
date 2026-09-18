"""Practice recursion."""


def factorial(number):
    """Return number factorial recursively."""
    if number < 0:
        raise ValueError("number must be non-negative")
    if number < 2:
        return 1
    return number * factorial(number - 1)


def main():
    print(factorial(int(input("Number: "))))


if __name__ == "__main__":
    main()
