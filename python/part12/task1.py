"""Practice type inspection."""

def type_name(value):
    """Return the built-in type name."""
    return type(value).__name__

def main():
    print(type_name(input("Value: ")))

if __name__ == "__main__":
    main()
