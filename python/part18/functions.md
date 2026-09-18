# Part 18: If and nested-if statements

This part practices single decisions and nested decisions.

## Practice files

- `task1.py`: check age eligibility.
- `task2.py`: choose a login result.
- `task3.py`: classify a score.
- `task4.py`: find the largest of three values.
- `mini_project.py`: validate a simple application.

The existing `if-else.py` and `nested-if-else.py` are reference examples.

## Original lesson content

### `if-else.py`
Checks an email, allows a second password attempt, and blocks the user after another incorrect password.

```python
if email == "nomannisar769@gmail.com":
	if password == "@Usama22":
		print("User login successfully!")
	else:
		print("Incorrect password!")
```

### `nested-if-else.py`
Combines email and password in a condition, then nests a retry branch for the correct email and incorrect password.