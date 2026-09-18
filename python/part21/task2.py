"""Task 2: generate a multiplication table with a function."""


def multiplication_table(number, limit=10):
    """Return multiplication results from 1 through limit."""
    return [number * multiplier for multiplier in range(1, limit + 1)]


def main():
    number = int(input("Enter number: "))
    for multiplier, result in enumerate(multiplication_table(number), start=1):
        print(f"{number} x {multiplier} = {result}")


if __name__ == "__main__":
    main()