"""Practice aggregation of objects."""


class Team:
    def __init__(self, members):
        self.members = []
        for member in members:
            self.members.append(member)

    def count(self):
        count = 0
        for _member in self.members:
            count += 1
        return count


def main():
    print(Team(input("Members: ").split(",")).count())


if __name__ == "__main__":
    main()
