"""Task 4: build a multiplication table without printing inside the helper."""


def table_as_text(number, limit=10):
    """Return a complete multiplication table as one text block."""
    return "\n".join(
        f"{number} x {multiplier} = {number * multiplier}"
        for multiplier in range(1, limit + 1)
    )


def main():
    number = int(input("Enter number: "))
    print(table_as_text(number))


if __name__ == "__main__":
    main()