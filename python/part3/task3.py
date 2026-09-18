"""Practice a closure and local scope."""


def make_counter(start=0):
    """Return a function that increments its private count."""
    count = start

    def next_value():
        nonlocal count
        count += 1
        return count

    return next_value


def main():
    counter = make_counter()
    print(counter(), counter())


if __name__ == "__main__":
    main()
