"""Practice counting in a loop."""


def count_even(numbers):
    """Return the number of even values."""
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def main():
    print(count_even(map(int, input("Numbers: ").split())))


if __name__ == "__main__":
    main()
