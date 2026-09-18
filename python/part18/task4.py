"""Practice a three-way comparison."""

def largest_of_three(first, second, third):
    """Return the largest of three values."""
    largest_value = first
    if second > largest_value:
        largest_value = second
    if third > largest_value:
        largest_value = third
    return largest_value

def main():
    values = [int(value) for value in input("Three values: ").split()]
    print(largest_of_three(*values))

if __name__ == "__main__":
    main()
