# Part 2: Control flow and function arguments

This part practices conditions, loops, type conversion, and positional, keyword, default, and variable-length arguments.

## Practice files

- `task1.py`: choose a message with a condition.
- `task2.py`: sum a sequence with a loop.
- `task3.py`: use a default argument.
- `task4.py`: collect variable-length arguments.
- `mini_project.py`: build a command-line bill calculator.

Existing examples in this folder cover the same syntax with small programs.

## Original lesson content

### `04_keywords_&_Identifiers.py`
Lists Python keywords and demonstrates valid identifiers such as `user_name` and `total_marks`.

### `06_type_conversion.py`
Converts strings to integers and floats and numbers back to strings.

```python
number_text = "25"
number = int(number_text)
price = float("19.5")
print(str(number), price)
```

### `07_Literals.py`
Demonstrates numeric, string, boolean, `None`, list, tuple, set, and dictionary literals.

```python
items = [1, "two", True]
record = {"name": "Nouman", "active": True}
```

### `conditions.py`
Uses `if`, `elif`, and `else` to classify positive, negative, and zero input.

```python
number = int(input("Enter number: "))
if number > 0:
	print("positive")
elif number < 0:
	print("negative")
else:
	print("zero")
```

### `loops.py`
Practices `for`, `while`, `break`, `continue`, factorials, prime checks, and reversing a string.

```python
for value in range(1, 6):
	print(value)
```

### `positional_arguments.py`, `keyword_arguments.py`, and `default_arguments.py`
Show positional calls, named calls, and defaults.

```python
def greet(name, message="Hello"):
	print(message, name)

greet("Nouman")
greet(name="Nouman", message="Welcome")
```

### `parameter_vs_arguments.py`
Distinguishes parameters in a definition from arguments supplied at a call site.

### `variable_length_arguments.py`
Uses `*args` and `**kwargs` for flexible calls.

```python
def show_values(*args, **kwargs):
	print(args)
	print(kwargs)
```

### `atm.py`
Reads a PIN, displays a balance, accepts deposits and withdrawals, and reports invalid choices.

```python
balance = 10000
if input("Enter pin: ") == "1234":
	print(balance)
```