# Part 10: Type conversion

This part practices converting between strings, integers, floats, and booleans.

## Practice files

- `task1.py`: convert text to an integer.
- `task2.py`: convert a number to a float.
- `task3.py`: parse a boolean word.
- `task4.py`: safely parse a number.
- `mini_project.py`: convert and summarize measurements.

`type_conversion.py` is the original example.

## Original lesson content

### `type_conversion.py`
Converts strings to integers and floats, numbers to strings, and inspects the resulting types.

```python
value = "10"
number = int(value)
decimal = float(value)
print(number, decimal, str(number))
```