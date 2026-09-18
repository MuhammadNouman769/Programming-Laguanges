"""Practice range-based multiplication."""

def factorial(number):
    """Return factorial using range."""
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

def main():
    print(factorial(int(input("Number: "))))

if __name__ == "__main__":
    main()
