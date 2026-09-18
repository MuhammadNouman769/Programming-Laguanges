"""Practice finding the largest value."""

def largest(values):
    """Return the largest value."""
    return max(values)

def main():
    print(largest([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
