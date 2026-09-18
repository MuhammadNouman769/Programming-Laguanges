# Part 13: Functions and lists

This part combines named functions with mutable list operations.

## Practice files

- `task1.py`: return a palindrome result.
- `task2.py`: transform a list.
- `task3.py`: split positive and negative values.
- `task4.py`: calculate a list average.
- `mini_project.py`: manage a shopping list.

`function.py` and `list.py` are the existing examples.

## Original lesson content

### `function.py`
Defines functions with parameters, return values, and calls.

```python
def add(first, second):
	return first + second

print(add(2, 3))
```

### `list.py`
Covers list creation, indexing, mutation, traversal, slicing, and methods including `append`, `insert`, `remove`, `pop`, `sort`, and `reverse`.

```python
items = [1, 2, 3]
items.append(4)
items[0] = 10
print(items[1:])
```