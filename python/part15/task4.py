"""Practice a prime-number check."""

def is_prime(number):
    """Return whether number is prime."""
    if number < 2:
        return False
    divisor = 2
    while divisor <= int(number ** 0.5):
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def main():
    print(is_prime(int(input("Number: "))))

if __name__ == "__main__":
    main()
