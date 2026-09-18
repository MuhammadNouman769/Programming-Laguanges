"""Practice a generator function."""


def countdown(start):
    """Yield integers from start down to one."""
    for number in range(start, 0, -1):
        yield number


def main():
    print(list(countdown(int(input("Start: ")))))


if __name__ == "__main__":
    main()
