"""Practice list partitioning."""

def partition(values):
    """Return positive and non-positive values separately."""
    return ([value for value in values if value > 0], [value for value in values if value <= 0])

def main():
    print(partition([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
