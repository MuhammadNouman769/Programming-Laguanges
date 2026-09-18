"""Practice a protected-style attribute."""


class User:
    def __init__(self, name):
        self._name = name

    def label(self):
        return self._name.title()


def main():
    print(User(input("Name: ")).label())


if __name__ == "__main__":
    main()
