"""Practice filtering with a predicate."""


def even_numbers(numbers):
    """Return only even numbers."""
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even


def main():
    values = [int(value) for value in input("Numbers: ").split()]
    print(even_numbers(values))


if __name__ == "__main__":
    main()
