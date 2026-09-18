"""Practice a three-way comparison."""

def largest_of_three(first, second, third):
    """Return the largest of three values."""
    return max(first, second, third)

def main():
    values = [int(value) for value in input("Three values: ").split()]
    print(largest_of_three(*values))

if __name__ == "__main__":
    main()
