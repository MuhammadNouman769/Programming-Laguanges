"""Mini project: calculate a simple bill."""


def subtotal(prices):
    """Return the total before tax."""
    return sum(prices)


def bill_total(prices, tax_rate=0.05):
    """Return subtotal plus a decimal tax rate."""
    return subtotal(prices) * (1 + tax_rate)


def main():
    prices = [float(value) for value in input("Prices: ").split()]
    print(f"Total: {bill_total(prices):.2f}")


if __name__ == "__main__":
    main()
