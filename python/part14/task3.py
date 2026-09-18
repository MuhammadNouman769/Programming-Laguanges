"""Practice list slicing."""

def rotate(values, amount=1):
    """Rotate values to the left by amount."""
    if not values:
        return []
    amount %= len(values)
    return values[amount:] + values[:amount]

def main():
    print(rotate(input("Values: ").split()))

if __name__ == "__main__":
    main()
