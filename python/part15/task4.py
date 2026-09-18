"""Practice a prime-number check."""

def is_prime(number):
    """Return whether number is prime."""
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))

def main():
    print(is_prime(int(input("Number: "))))

if __name__ == "__main__":
    main()
