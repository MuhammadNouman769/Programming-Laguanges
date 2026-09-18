"""Practice list transformation."""

def doubled(values):
    """Return every value multiplied by two."""
    return [value * 2 for value in values]

def main():
    print(doubled([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
