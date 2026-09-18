"""Mini project: generate a multiplication table."""

def table(number, start=1, end=10):
    """Return formatted table lines."""
    lines = []
    value = start
    while value <= end:
        lines.append(f"{number} x {value} = {number * value}")
        value += 1
    return lines

def main():
    print("\n".join(table(int(input("Number: ")))))

if __name__ == "__main__":
    main()
