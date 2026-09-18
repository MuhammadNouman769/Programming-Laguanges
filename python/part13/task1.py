"""Practice a function with a boolean result."""

def is_palindrome(text):
    """Return whether normalized text reads the same backwards."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def main():
    print(is_palindrome(input("Text: ")))

if __name__ == "__main__":
    main()
