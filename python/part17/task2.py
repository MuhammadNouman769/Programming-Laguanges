"""Practice guess comparison."""

def hint(secret, guess):
    """Return low, high, or correct."""
    return "correct" if guess == secret else "too low" if guess < secret else "too high"

def main():
    print(hint(int(input("Secret: ")), int(input("Guess: "))))

if __name__ == "__main__":
    main()
