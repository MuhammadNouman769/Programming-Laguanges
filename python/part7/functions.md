# Part 7: Classes and object relationships

This part practices classes, modifiers, association, and aggregation.

## Practice files

- `task1.py`: define an object with state.
- `task2.py`: use a protected-style attribute.
- `task3.py`: associate two objects.
- `task4.py`: aggregate objects in a team.
- `mini_project.py`: manage a small library.

The existing class, modifiers, and association files are reference examples.

## Original lesson content

### `class.py`
Creates classes with attributes, methods, constructors, and object instances.

```python
class Person:
	def __init__(self, name):
		self.name = name

	def display(self):
		print(self.name)
```

### `modifiers.py`
Explains public, protected-style (`_name`), and private (`__name`) attributes and access through methods.

### `association_aggregation.py`
Models one object using another and shows aggregation, where the contained object can exist independently.