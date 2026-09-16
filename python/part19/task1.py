
# Task 1 — Marks & Grade

# User se marks input lo:

# Enter your marks: 78

# Rules:

# 90 - 100 → A+
# 80 - 89 → A
# 70 - 79 → B
# 60 - 69 → C
# 50 - 59 → D
# < 50 → Fail
# > 100 ya < 0 → Invalid marks
while True:
    marks = int(input('Enter your Marks get result:-'))

    if marks < 0 or marks > 100:
        print('Invalid marks')
    elif marks >= 90:
        print('A+')
    elif marks >= 80:
        print('A')
    elif marks >= 70:
        print('B')
    elif marks >= 60:
        print('C')
    elif marks >= 50:
        print('D')
    else:
        print('Fail')