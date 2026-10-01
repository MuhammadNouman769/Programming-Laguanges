import json
from abc import ABC, abstractmethod
from os.path import exists

DATABASE = "school_data.json"
data = {"students": [], "teachers": []}

if exists(DATABASE):
    with open(DATABASE, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


def save():
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


class Person(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" not in email:
            return False
        domain = email.split("@")[-1]
        return "." in domain and not email.startswith("@")


class Student(Person):

    def get_roles(self):
        return "students"

    def show_details(self):
        for student in data[self.get_roles()]:
            print(f"{student['roll_no']} | {student['name']} | "
                  f"{student['age']} | {student['email']}")

    def register(self):
        name = input("Tell your name :- ").strip()

        while True:
            try:
                age = int(input("Tell your age :- "))
                break
            except ValueError:
                print("Age number mein likhein.")

        while True:
            email = input("Tell your email :- ").strip()
            if Person.validate_email(email):
                break
            print("Invalid email format. Try again.")

        roll_no = input("Tell your roll number :- ").strip()
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                print("Roll number already exists.")
                return

        data["students"].append({
            "name": name,
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grade": {}
        })
        save()
        print(f"Student {name} registered successfully.")


stud = Student()

while True:
    print("\n1. Register student\n2. Show students\n0. Exit")
    choice = input("Enter your choice :- ").strip()

    if choice == "1":
        stud.register()
    elif choice == "2":
        stud.show_details()
    elif choice == "0":
        break
    else:
        print("Invalid choice.")