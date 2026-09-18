"""Practice finding the smallest value."""

def smallest(values):
    """Return the smallest value."""
    return min(values)

def main():
    print(smallest([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
