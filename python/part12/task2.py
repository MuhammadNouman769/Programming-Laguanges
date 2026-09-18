"""Practice sequence operations."""

def item_count(items):
    """Return the number of items."""
    return len(items)

def main():
    print(item_count(input("Items: ").split()))

if __name__ == "__main__":
    main()
