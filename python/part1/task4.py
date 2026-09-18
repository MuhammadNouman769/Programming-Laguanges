"""Practice converting user input."""


def to_integer(text):
    """Convert text to an integer."""
    return int(text.strip())


def main():
    print(to_integer(input("Integer: ")))


if __name__ == "__main__":
    main()
