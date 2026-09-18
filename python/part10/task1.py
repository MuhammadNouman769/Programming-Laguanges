"""Practice integer conversion."""

def parse_integer(text):
    """Convert trimmed text to an integer."""
    return int(text.strip())

def main():
    print(parse_integer(input("Integer: ")))

if __name__ == "__main__":
    main()
