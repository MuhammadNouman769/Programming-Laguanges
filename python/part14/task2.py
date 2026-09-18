"""Practice list extremes."""

def extremes(values):
    """Return minimum and maximum."""
    return min(values), max(values)

def main():
    print(extremes([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
