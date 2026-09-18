"""Practice list statistics."""

def mean(values):
    """Return the average of values."""
    if not values:
        raise ValueError("values cannot be empty")
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

def main():
    print(mean([float(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
