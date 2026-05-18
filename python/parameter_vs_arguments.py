# ============================================
# 1. BASIC FUNCTION WITH DIFFERENT ARGUMENT TYPES
# ============================================
def student(name, age, roll_no):
    print(f"{name} is {age} years old and has roll number {roll_no}")

print("--- Positional Arguments ---")
student("shanzy", 20, 12345)

print("\n--- Keyword Arguments ---")
student(name="shanzy", age=20, roll_no=54321)

print("\n--- Mixed Arguments ---")
student("shanzy", age=25, roll_no=67890)


# ============================================
# 2. *ARGS (Multiple Positional Arguments)
# ============================================
def sum_total(*args):
    total = 0
    print(f"Arguments received: {args}")  # args is a TUPLE
    for n in args:
        total += n
    return total

print("\n--- *args Example ---")
result = sum_total(1, 2, 3, 4, 5)
print(f"Sum: {result}")  # Output: Sum: 15


# ============================================
# 3. **KWARGS (Multiple Keyword Arguments)
# ============================================
def my_detail(**kwargs):
    print(f"Keyword arguments received: {kwargs}")  # kwargs is a DICT
    for key, value in kwargs.items():
        print(f"{key} → {value}")

print("\n--- **kwargs Example ---")
my_detail(name="Nouman", age=20, city="Karachi", profession="Developer")


# ============================================
# 4. ALL TOGETHER (args + kwargs)
# ============================================
def complete_example(*args, **kwargs):
    print(f"Positional arguments (*args): {args}")
    print(f"Keyword arguments (**kwargs): {kwargs}")
    
    total = sum(args)
    print(f"Sum of positional arguments: {total}")
    
    for key, value in kwargs.items():
        print(f"Keyword - {key}: {value}")

print("\n--- *args and **kwargs Together ---")
complete_example(10, 20, 30, name="Ali", age=25, city="Lahore")
# Output:
# Positional arguments (*args): (10, 20, 30)
# Keyword arguments (**kwargs): {'name': 'Ali', 'age': 25, 'city': 'Lahore'}