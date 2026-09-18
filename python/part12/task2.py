"""Practice sequence operations."""

def item_count(items):
    """Return the number of items."""
    count = 0
    for _item in items:
        count += 1
    return count

def main():
    print(item_count(input("Items: ").split()))

if __name__ == "__main__":
    main()
