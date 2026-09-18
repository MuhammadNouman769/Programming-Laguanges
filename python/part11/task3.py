"""Practice case and whitespace normalization."""

def title(text):
    """Return a trimmed title-cased string."""
    return text.strip().title()

def main():
    print(title(input("Title: ")))

if __name__ == "__main__":
    main()
