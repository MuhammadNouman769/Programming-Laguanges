"""Practice string classification."""


def text_kind(text):
    """Return whether text is blank, numeric, or general text."""
    if not text:
        return "blank"
    return "numeric" if text.isdigit() else "text"


def main():
    print(text_kind(input("Text: ")))


if __name__ == "__main__":
    main()
