"""Practice detecting duplicate values."""

def duplicates(values):
    """Return values appearing more than once."""
    duplicates_found = []
    for value in values:
        occurrences = 0
        for item in values:
            if item == value:
                occurrences += 1
        already_added = False
        for saved_value in duplicates_found:
            if saved_value == value:
                already_added = True
                break
        if occurrences > 1 and not already_added:
            duplicates_found.append(value)
    index = 1
    duplicate_count = 0
    for _value in duplicates_found:
        duplicate_count += 1
    while index < duplicate_count:
        current = duplicates_found[index]
        previous = index - 1
        while previous >= 0 and duplicates_found[previous] > current:
            duplicates_found[previous + 1] = duplicates_found[previous]
            previous -= 1
        duplicates_found[previous + 1] = current
        index += 1
    return duplicates_found

def main():
    print(duplicates(input("Values: ").split()))

if __name__ == "__main__":
    main()
