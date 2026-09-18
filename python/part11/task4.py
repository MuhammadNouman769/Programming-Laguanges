"""Practice slicing."""

def middle(text):
    """Return the middle half of text."""
    start = len(text) // 4
    end = len(text) - start
    return text[start:end]

def main():
    print(middle(input("Text: ")))

if __name__ == "__main__":
    main()
