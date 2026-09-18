# Part 14: Lists and ranges

This part practices list methods, ranges, traversal, and numeric sequences.

## Practice files

- `task1.py`: build a range list.
- `task2.py`: find list extremes.
- `task3.py`: rotate a list.
- `task4.py`: calculate a factorial with range.
- `mini_project.py`: generate a multiplication table.

The existing list and range files are longer practice examples.

## Original lesson content

### `list.py`
Demonstrates mutable lists, mixed and duplicate values, indexed traversal, slicing, and CRUD methods.

```python
items = [1, 2, 3, "hello"]
items.append(4)
items[0] = 10
print(items[1:])
```

### `list_practice.py`
Applies list traversal, membership checks, and list calculations to small exercises.

### `range.py`
Uses `range(start, stop, step)` for ascending and descending sequences.

```python
for number in range(1, 10, 2):
	print(number)
```