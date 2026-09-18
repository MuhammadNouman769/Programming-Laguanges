"""Practice attempt counting."""

def attempts_until(history, secret):
    """Return attempts through the first correct guess."""
    for count, guess in enumerate(history, 1):
        if guess == secret:
            return count
    return None

def main():
    guesses = [int(value) for value in input("Guesses: ").split()]
    print(attempts_until(guesses, int(input("Secret: "))))

if __name__ == "__main__":
    main()
