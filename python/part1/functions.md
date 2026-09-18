# Part 1: Python basics

This part introduces Python syntax, variables, output, comments, data types, and user input. Functions keep calculations reusable and let `main()` handle interaction.

## Practice files

- `task1.py`: format a greeting.
- `task2.py`: describe a value and its type.
- `task3.py`: calculate a rectangle area.
- `task4.py`: convert text input to a number.
- `mini_project.py`: build a small profile summary.

Keep input inside `main()` and return values from helper functions.

## Original lesson content

### `what_is _python.py`
Introduces Python as a high-level language and prints a greeting.

```python
print("Hello world")
```

### `variables.py`
Demonstrates assigning and reassigning names, naming rules, and arithmetic expressions.

```python
name = "Nouman"
age = 22
age = age + 1
print(name, age)
```

### `data_types.py`
Creates integer, float, complex, boolean, string, list, tuple, set, and dictionary values and inspects them with `type()`.

```python
integer_value = 10
decimal_value = 3.14
text = "Python"
items = [1, 2, 3]
print(type(integer_value), type(decimal_value), type(text), type(items))
```

### `user_input.py`
Reads text input and converts numeric input with `int()`.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"{name} is {age} years old")
```

### `print.py`
Practices `print()` with multiple arguments, separators, and formatted strings.

```python
print("Hello", "Python", sep=" ")
print("Name: {}".format("Nouman"))
```

### `comments.py`
Distinguishes single-line comments from triple-quoted documentation text.

```python
# This is a comment.
"""This text documents a module or function."""
```