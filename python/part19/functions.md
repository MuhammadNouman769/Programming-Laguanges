# Part 19: Grades and ATM practice

This part practices validation, grade decisions, and simple transaction flows.

## Practice files

- `task1.py`, `task2.py`, `task3.py`: existing grade and task exercises.
- `task4.py`: validate an ATM withdrawal.
- `mini_project.py`: model a small account.

## Original lesson content

### `mini-atm-project.py`
Starts with a balance of 10000, asks for a PIN, displays balance, accepts deposits and withdrawals, checks insufficient funds, and offers an exit option. The canonical `mini_project.py` now provides the same lesson as a runnable PIN login with three attempts and an ATM menu.

```python
balance = 10000
pin = input("Enter pin: ")
if pin == "1234":
	print("login successfully!")
```