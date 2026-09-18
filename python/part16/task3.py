"""Practice membership operators."""

def contains(items, value):
    """Return whether value is in items."""
    return value in items

def main():
    print(contains(input("Items: ").split(), input("Value: ")))

if __name__ == "__main__":
    main()
