"""Mini project: an interactive multiplication-table generator."""


def make_table(number, start=1, end=10):
    """Return table lines for the inclusive multiplier range."""
    if start > end:
        raise ValueError("start must not be greater than end")
    lines = []
    multiplier = start
    while multiplier <= end:
        lines.append(f"{number} x {multiplier} = {number * multiplier}")
        multiplier += 1
    return lines


def read_integer(prompt, default=None):
    """Read an integer, optionally using a default for blank input."""
    value = input(prompt).strip()
    if not value and default is not None:
        return default
    return int(value)


def main():
    number = read_integer("Number: ")
    start = read_integer("Start multiplier [1]: ", default=1)
    end = read_integer("End multiplier [10]: ", default=10)
    print("\n".join(make_table(number, start, end)))


if __name__ == "__main__":
    main()