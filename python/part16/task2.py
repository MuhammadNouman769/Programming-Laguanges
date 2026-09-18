"""Practice comparison operators."""

def compare(left, right):
    """Return useful comparison results."""
    return {"equal": left == right, "less": left < right, "greater": left > right}

def main():
    print(compare(float(input("Left: ")), float(input("Right: "))))

if __name__ == "__main__":
    main()
