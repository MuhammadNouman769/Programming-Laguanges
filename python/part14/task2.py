"""Practice list extremes."""

def extremes(values):
    """Return minimum and maximum."""
    smallest_value = values[0]
    largest_value = values[0]
    for value in values:
        if value < smallest_value:
            smallest_value = value
        if value > largest_value:
            largest_value = value
    return smallest_value, largest_value

def main():
    print(extremes([int(value) for value in input("Values: ").split()]))

if __name__ == "__main__":
    main()
