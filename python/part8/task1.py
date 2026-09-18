"""Practice a for loop."""


def table(number, limit=10):
    """Return multiplication results."""
    results = []
    multiplier = 1
    while multiplier <= limit:
        results.append(number * multiplier)
        multiplier += 1
    return results


def main():
    print(table(int(input("Number: "))))


if __name__ == "__main__":
    main()
