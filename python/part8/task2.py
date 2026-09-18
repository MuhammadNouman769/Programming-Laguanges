"""Practice counting in a loop."""


def count_even(numbers):
    """Return the number of even values."""
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def main():
    numbers = []
    for value in input("Numbers: ").split():
        numbers.append(int(value))
    print(count_even(numbers))


if __name__ == "__main__":
    main()
