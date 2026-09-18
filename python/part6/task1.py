"""Practice single inheritance."""


class Person:
    def greet(self):
        return "hello"


class Student(Person):
    pass


def main():
    print(Student().greet())


if __name__ == "__main__":
    main()
