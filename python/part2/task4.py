"""Practice variable-length arguments."""


def average(*numbers):
    """Return the arithmetic mean of numbers."""
    if not numbers:
        raise ValueError("at least one number is required")
    return sum(numbers) / len(numbers)


def main():
    values = [float(value) for value in input("Numbers: ").split()]
    print(average(*values))


if __name__ == "__main__":
    main()
