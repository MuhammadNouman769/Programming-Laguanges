"""Practice a generator function."""


def countdown(start):
    """Yield integers from start down to one."""
    number = start
    while number > 0:
        yield number
        number -= 1


def main():
    values = []
    for number in countdown(int(input("Start: "))):
        values.append(number)
    print(values)


if __name__ == "__main__":
    main()
