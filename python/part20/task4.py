"""Practice finding the largest value."""

def largest(values):
    """Return the largest value."""
    largest_value = values[0]
    for value in values:
        if value > largest_value:
            largest_value = value
    return largest_value

def main():
    print(largest([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
