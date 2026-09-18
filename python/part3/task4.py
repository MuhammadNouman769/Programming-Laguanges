"""Practice filtering with a predicate."""


def even_numbers(numbers):
    """Return only even numbers."""
    return list(filter(lambda number: number % 2 == 0, numbers))


def main():
    values = [int(value) for value in input("Numbers: ").split()]
    print(even_numbers(values))


if __name__ == "__main__":
    main()
