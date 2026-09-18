"""Mini project: represent inherited staff roles."""


class Staff:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"Staff: {self.name}"


class Developer(Staff):
    def description(self):
        return f"Developer: {self.name}"


def main():
    print(Developer(input("Name: ")).description())


if __name__ == "__main__":
    main()
