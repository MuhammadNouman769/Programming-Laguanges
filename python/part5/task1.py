"""Practice a total function."""


def total(values):
    """Return the sum of values."""
    result = 0
    for value in values:
        result += value
    return result


def main():
    print(total([int(value) for value in input("Values: ").split()]))


if __name__ == "__main__":
    main()
