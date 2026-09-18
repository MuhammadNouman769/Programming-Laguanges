"""Practice a total function."""


def total(values):
    """Return the sum of values."""
    return sum(values)


def main():
    print(total([int(value) for value in input("Values: ").split()]))


if __name__ == "__main__":
    main()
