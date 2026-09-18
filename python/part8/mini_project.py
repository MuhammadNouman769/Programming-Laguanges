"""Mini project: analyze a sequence with loops."""


def analyze(numbers):
    """Return count, total, and maximum for numbers."""
    numbers = list(numbers)
    return {"count": len(numbers), "total": sum(numbers), "maximum": max(numbers, default=None)}


def main():
    print(analyze(map(int, input("Numbers: ").split())))


if __name__ == "__main__":
    main()
