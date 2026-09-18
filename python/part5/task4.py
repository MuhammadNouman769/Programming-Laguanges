"""Practice repetition."""


def repeat(message, count):
    """Return message repeated count times."""
    return [message] * count


def main():
    print(repeat(input("Message: "), int(input("Count: "))))


if __name__ == "__main__":
    main()
