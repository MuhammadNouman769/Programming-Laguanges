"""Practice method resolution order."""


class Root:
    def name(self):
        return "root"


class Branch(Root):
    def name(self):
        return f"branch -> {super().name()}"


def main():
    print(Branch.mro())
    print(Branch().name())


if __name__ == "__main__":
    main()
