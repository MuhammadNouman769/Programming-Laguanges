"""Practice arithmetic operators."""

def arithmetic(left, right):
    """Return common arithmetic results."""
    return {"sum": left + right, "difference": left - right, "product": left * right}

def main():
    print(arithmetic(float(input("Left: ")), float(input("Right: "))))

if __name__ == "__main__":
    main()
