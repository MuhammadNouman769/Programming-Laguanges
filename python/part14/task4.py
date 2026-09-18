"""Practice range-based multiplication."""

def factorial(number):
    """Return factorial using range."""
    result = 1
    value = 1
    while value <= number:
        result *= value
        value += 1
    return result

def main():
    print(factorial(int(input("Number: "))))

if __name__ == "__main__":
    main()
