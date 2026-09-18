"""Practice values and built-in types."""


def describe_value(value):
    """Return a short description of a value."""
    return f"value={value!r}, type={type(value).__name__}"


def main():
    print(describe_value(input("Value: ")))


if __name__ == "__main__":
    main()
