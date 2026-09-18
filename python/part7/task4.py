"""Practice aggregation of objects."""


class Team:
    def __init__(self, members):
        self.members = list(members)

    def count(self):
        return len(self.members)


def main():
    print(Team(input("Members: ").split(",")).count())


if __name__ == "__main__":
    main()
