"""Practice loops and accumulation."""


def total(numbers):
    """Return the sum of numbers."""
    result = 0
    for number in numbers:
        result += number
    return result


def main():
    values = [int(value) for value in input("Numbers: ").split()]
    print(total(values))


if __name__ == "__main__":
    main()
