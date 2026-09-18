"""Practice default function arguments."""


def power(number, exponent=2):
    """Raise number to exponent, defaulting to a square."""
    return number ** exponent


def main():
    print(power(float(input("Number: "))))


if __name__ == "__main__":
    main()
