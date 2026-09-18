"""Practice round scoring."""

def score(secret, guesses):
    """Return one point for each exact guess."""
    score_total = 0
    for guess in guesses:
        if guess == secret:
            score_total += 1
    return score_total

def main():
    guesses = []
    for value in input("Guesses: ").split():
        guesses.append(int(value))
    print(score(int(input("Secret: ")), guesses))

if __name__ == "__main__":
    main()
