"""Mini project: build a typed inventory."""

def inventory_item(name, quantity, price):
    """Return one inventory record."""
    return {"name": str(name), "quantity": int(quantity), "price": float(price)}

def inventory_value(item):
    """Return the value of an inventory record."""
    return item["quantity"] * item["price"]

def main():
    item = inventory_item(input("Name: "), input("Quantity: "), input("Price: "))
    print(item, inventory_value(item))

if __name__ == "__main__":
    main()
