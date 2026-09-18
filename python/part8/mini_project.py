"""Mini project: analyze a sequence with loops."""


def analyze(numbers):
    """Return count, total, and maximum for numbers."""
    count = 0
    total = 0
    maximum = None
    for number in numbers:
        count += 1
        total += number
        if maximum is None or number > maximum:
            maximum = number
    return {"count": count, "total": total, "maximum": maximum}


def main():
    numbers = []
    for value in input("Numbers: ").split():
        numbers.append(int(value))
    print(analyze(numbers))


if __name__ == "__main__":
    main()
