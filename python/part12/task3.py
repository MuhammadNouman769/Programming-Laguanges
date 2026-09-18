"""Practice set uniqueness."""

def unique(items):
    """Return sorted unique items."""
    return sorted(set(items))

def main():
    print(unique(input("Items: ").split()))

if __name__ == "__main__":
    main()
