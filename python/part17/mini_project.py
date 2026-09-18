"""Mini project: a random number guessing game."""

import random

def play_game(maximum, attempts_allowed):
    secret = random.randint(1, maximum)
    attempts = 0
    while attempts < attempts_allowed:
        try:
            guess = int(input(f"Guess 1-{maximum} ({attempts + 1}/{attempts_allowed}): "))
        except ValueError:
            print("Enter a valid number.")
            continue
        if not 1 <= guess <= maximum:
            print("Guess is outside the range.")
            continue
        attempts += 1
        if guess == secret:
            print(f"Correct in {attempts} attempts.")
            return
        print("Too low." if guess < secret else "Too high.")
    print(f"Game over. The number was {secret}.")

def main():
    levels = {"1": (50, 10), "2": (100, 7), "3": (200, 5)}
    choice = input("Difficulty 1 Easy, 2 Medium, 3 Hard: ").strip()
    maximum, attempts = levels.get(choice, levels["1"])
    play_game(maximum, attempts)

if __name__ == "__main__":
    main()
