"""Practice round scoring."""

def score(secret, guesses):
    """Return one point for each exact guess."""
    return sum(guess == secret for guess in guesses)

def main():
    print(score(int(input("Secret: ")), map(int, input("Guesses: ").split())))

if __name__ == "__main__":
    main()
