"""Practice a bounded secret number."""

def secret_number(seed, limit=10):
    """Return a repeatable number in the game range."""
    return seed % limit + 1

def main():
    print(secret_number(int(input("Seed: "))))

if __name__ == "__main__":
    main()
