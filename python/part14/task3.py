"""Practice list slicing."""

def rotate(values, amount=1):
    """Rotate values to the left by amount."""
    if not values:
        return []
    count = 0
    for _value in values:
        count += 1
    amount %= count
    return values[amount:] + values[:amount]

def main():
    print(rotate(input("Values: ").split()))

if __name__ == "__main__":
    main()
