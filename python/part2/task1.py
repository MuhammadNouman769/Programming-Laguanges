"""Practice a conditional function."""


def sign_label(number):
    """Return whether number is negative, zero, or positive."""
    if number < 0:
        return "negative"
    if number > 0:
        return "positive"
    return "zero"


def main():
    print(sign_label(int(input("Number: "))))


if __name__ == "__main__":
    main()
