# Part 17: Beginner projects

This part uses functions to structure small interactive projects such as guessing games.

## Practice files

- `task1.py`: generate a secret number.
- `task2.py`: compare a guess.
- `task3.py`: count attempts.
- `task4.py`: score a round.
- `mini_project.py`: run a deterministic guessing game.

Existing `number_guessing_game.py` and `mini_project2.py` remain unchanged.

## Original lesson content

### `number_guessing_game.py`
Chooses a random number, supports easy, medium, and hard ranges, validates guesses, gives too-high and too-low hints, limits attempts, and supports replay. The runnable migrated implementation is in `mini_project.py`.

```python
secret_number = random.randint(1, max_num)
if guess < secret_number:
	print("Too Low")
elif guess > secret_number:
	print("Too High")
```

### `mini_project2.py`
Imports `main` from the guessing game and calls it under a `__main__` guard. That behavior is retained directly by the canonical mini project.