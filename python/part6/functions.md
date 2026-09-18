# Part 6: Inheritance

This part studies single, multiple, multilevel, hierarchical inheritance and method resolution order.

## Practice files

- `task1.py`: inherit a greeting method.
- `task2.py`: extend a base class.
- `task3.py`: combine two parent behaviors.
- `task4.py`: inspect method resolution order.
- `mini_project.py`: model inherited staff roles.

The existing inheritance files remain as reference examples.

## Original lesson content

### `single_inheritance.py`, `multilevel_inheritance_03.py`, and `hierarchical_inheritance.py`
Define parent and child classes, extending behavior through one level, several levels, or several children.

```python
class Animal:
	def speak(self):
		return "sound"

class Dog(Animal):
	def speak(self):
		return "bark"
```

### `multiple_inheritance.py` and `diamond_problem.py`
Inherit from multiple parents and demonstrate how the diamond shape is resolved by method resolution order.

### `mro.py`
Prints `ClassName.mro()` and `ClassName.__mro__`.

### `inheritance.py`
Combines parent methods, overridden child methods, `super()`, and constructors in a larger inheritance example.