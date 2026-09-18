# Part 15: Python interview practice

This part reviews common Python concepts through small reusable functions: types, collections, and basic algorithms.

## Practice files

- `task1.py`: count word frequencies.
- `task2.py`: find duplicates.
- `task3.py`: flatten a list.
- `task4.py`: test a prime number.
- `mini_project.py`: create an interview revision scorecard.

`python_interview_preparation.py` contains the original notes.

## Original lesson content

### `python_interview_preparation.py`
The original notes explain Python as a high-level language; numeric, sequence, text, set, mapping, boolean, and binary data types; mutable versus immutable values; implicit and explicit type casting; functions; lambda functions; and indexing versus slicing.

```python
my_list = [1, 2, 3]
my_list[0] = 10
my_tuple = (1, 2, 3)
number = 10
decimal = 3.14
print(number + decimal, type(number + decimal))
square = lambda value: value ** 2
print(square(5))
```