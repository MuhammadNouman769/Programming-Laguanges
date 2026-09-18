"""Mini project: generate a multiplication table."""

def table(number, start=1, end=10):
    """Return formatted table lines."""
    return [f"{number} x {value} = {number * value}" for value in range(start, end + 1)]

def main():
    print("\n".join(table(int(input("Number: ")))))

if __name__ == "__main__":
    main()
