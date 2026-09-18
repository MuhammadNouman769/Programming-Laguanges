"""Practice detecting duplicate values."""

def duplicates(values):
    """Return values appearing more than once."""
    return sorted({value for value in values if values.count(value) > 1})

def main():
    print(duplicates(input("Values: ").split()))

if __name__ == "__main__":
    main()
