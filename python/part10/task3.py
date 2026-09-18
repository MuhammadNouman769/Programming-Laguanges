"""Practice boolean conversion."""

def parse_bool(text):
    """Parse common true and false words."""
    value = text.strip().lower()
    if value in {"true", "yes", "1"}:
        return True
    if value in {"false", "no", "0"}:
        return False
    raise ValueError("expected a boolean word")

def main():
    print(parse_bool(input("True or false: ")))

if __name__ == "__main__":
    main()
