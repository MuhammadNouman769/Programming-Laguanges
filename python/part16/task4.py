"""Practice percentage arithmetic."""

def discount(price, percent):
    """Return price after a percentage discount."""
    return price * (1 - percent / 100)

def main():
    print(discount(float(input("Price: ")), float(input("Discount percent: "))))

if __name__ == "__main__":
    main()
