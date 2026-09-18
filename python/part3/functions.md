# Part 3: Lambda functions and scope

This part explores short anonymous functions and the difference between local and global names.

## Practice files

- `task1.py`: create a square lambda.
- `task2.py`: sort records with a key function.
- `task3.py`: demonstrate a closure.
- `task4.py`: filter values with a predicate.
- `mini_project.py`: summarize scores with functional helpers.

Existing `lambda_function.py` and `scope.py` are topic examples.

## Original lesson content

### `lambda_function.py`
Defines anonymous functions and applies them to simple calculations, including `map`, `filter`, and `reduce` examples.

```python
square = lambda number: number * number
print(square(5))
```

### `scope.py`
Demonstrates local, global, and enclosing variables with nested functions.

```python
message = "global"

def show_scope():
	message = "local"
	print(message)
```