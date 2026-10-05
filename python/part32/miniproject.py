

students = [
    {"name": "Ali", "marks": 80},
    {"name": "Usman", "marks": 45},
    {"name": "Ahmed", "marks": 70},
    {"name": "Hamza", "marks": 35},
]

passed = [
    student["name"]
    for student in students
    if student["marks"] >= 50
]
print(passed)


students = [
    {"name": "Ali", "marks": 80},
    {"name": "Usman", "marks": 45},
    {"name": "Ahmed", "marks": 70},
    {"name": "Hamza", "marks": 35},
]
passed = [
    student["name"]
    for student in students
    if student["marks"] >= 50
]
print(passed)