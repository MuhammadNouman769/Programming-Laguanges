"""Practice number classification."""


def classify(number):
    """Return positive, negative, or zero."""
    return "positive" if number > 0 else "negative" if number < 0 else "zero"


def main():
    print(classify(int(input("Number: "))))


if __name__ == "__main__":
    main()
