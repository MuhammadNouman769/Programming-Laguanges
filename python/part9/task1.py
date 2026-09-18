"""Practice comparisons."""


def compare(left, right):
    """Return the relationship between two values."""
    if left < right:
        return "less"
    if left > right:
        return "greater"
    return "equal"


def main():
    print(compare(int(input("Left: ")), int(input("Right: "))))


if __name__ == "__main__":
    main()
