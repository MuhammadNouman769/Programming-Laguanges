"""Practice attempt counting."""

def attempts_until(history, secret):
    """Return attempts through the first correct guess."""
    count = 1
    for guess in history:
        if guess == secret:
            return count
        count += 1
    return None

def main():
    guesses = [int(value) for value in input("Guesses: ").split()]
    print(attempts_until(guesses, int(input("Secret: "))))

if __name__ == "__main__":
    main()
