"""Practice float conversion."""

def parse_float(text):
    """Convert text to a floating-point number."""
    return float(text.strip())

def main():
    print(parse_float(input("Decimal: ")))

if __name__ == "__main__":
    main()
