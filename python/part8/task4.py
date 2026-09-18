"""Practice reverse traversal."""


def reverse_text(text):
    """Return text in reverse order."""
    result = ""
    for character in text:
        result = character + result
    return result


def main():
    print(reverse_text(input("Text: ")))


if __name__ == "__main__":
    main()
