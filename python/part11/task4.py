"""Practice slicing."""

def middle(text):
    """Return the middle half of text."""
    length = 0
    for _character in text:
        length += 1
    start = length // 4
    end = length - start
    return text[start:end]

def main():
    print(middle(input("Text: ")))

if __name__ == "__main__":
    main()
