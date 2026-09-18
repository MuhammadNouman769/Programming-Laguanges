"""Task 3: return a formatted multiplication table."""


def formatted_table(number, limit=10):
    """Return table lines suitable for printing or saving to a file."""
    return [
        f"{number} x {multiplier} = {number * multiplier}"
        for multiplier in range(1, limit + 1)
    ]


def main():
    number = int(input("Enter number: "))
    print("\n".join(formatted_table(number)))


if __name__ == "__main__":
    main()