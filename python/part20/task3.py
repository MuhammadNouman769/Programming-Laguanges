"""Practice finding the smallest value."""

def smallest(values):
    """Return the smallest value."""
    smallest_value = values[0]
    for value in values:
        if value < smallest_value:
            smallest_value = value
    return smallest_value

def main():
    print(smallest([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
