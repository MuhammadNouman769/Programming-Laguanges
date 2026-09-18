"""Practice a small class."""


class Counter:
    """Store and increment a count."""

    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value


def main():
    counter = Counter()
    print(counter.increment())


if __name__ == "__main__":
    main()
