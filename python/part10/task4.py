"""Practice guarded conversion."""

def try_number(text):
    """Return a float or None when conversion fails."""
    try:
        return float(text)
    except ValueError:
        return None

def main():
    print(try_number(input("Number: ")))

if __name__ == "__main__":
    main()
