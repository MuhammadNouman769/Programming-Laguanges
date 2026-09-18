"""Mini project: summarize a set of numbers."""

def summarize(values):
    """Return basic comparison statistics."""
    numbers = []
    for value in values:
        numbers.append(value)
    smallest_value = numbers[0]
    largest_value = numbers[0]
    for value in numbers:
        if value < smallest_value:
            smallest_value = value
        if value > largest_value:
            largest_value = value
    return {"smallest": smallest_value, "largest": largest_value, "range": largest_value - smallest_value}

def main():
    values = []
    for value in input("Values: ").split():
        values.append(int(value))
    print(summarize(values))

if __name__ == "__main__":
    main()
