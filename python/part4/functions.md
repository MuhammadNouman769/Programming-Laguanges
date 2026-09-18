# Part 4: Advanced functions and OOP

This part covers decorators, generators, iterators, recursion, copying, and classes.

## Practice files

- `task1.py`: generate values lazily.
- `task2.py`: recurse over a number.
- `task3.py`: wrap a function with a decorator.
- `task4.py`: model a small object.
- `mini_project.py`: create a task queue with a generator.

Existing files provide longer examples for each concept.

## Original lesson content

### `decorators.py`
Wraps a function and runs code before and after the wrapped call.

```python
def logger(function):
	def wrapper(*args, **kwargs):
		print("starting")
		result = function(*args, **kwargs)
		print("finished")
		return result
	return wrapper
```

### `generators.py` and `iterable_vs_iterator.py`
Use `yield`, `iter()`, and `next()` to produce values lazily.

```python
def count_to(limit):
	for number in range(1, limit + 1):
		yield number

iterator = iter([1, 2, 3])
print(next(iterator))
```

### `recursion.py`
Calculates a factorial recursively.

```python
def factorial(number):
	if number <= 1:
		return 1
	return number * factorial(number - 1)
```

### `deep_copy_shallow_copy.py`
Compares `copy.copy()` and `copy.deepcopy()` for nested lists.

### `oop.py`
Defines classes with constructors, attributes, methods, and instances.

```python
class Student:
	def __init__(self, name):
		self.name = name

	def introduce(self):
		return f"I am {self.name}"
```