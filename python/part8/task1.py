"""Practice a for loop."""


def table(number, limit=10):
    """Return multiplication results."""
    return [number * multiplier for multiplier in range(1, limit + 1)]


def main():
    print(table(int(input("Number: "))))


if __name__ == "__main__":
    main()
