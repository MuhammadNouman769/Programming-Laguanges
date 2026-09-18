"""Practice list statistics."""

def mean(values):
    """Return the average of values."""
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

def main():
    print(mean([float(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
