"""Mini project: manage a shopping list."""

def add_item(items, item):
    """Return a new list with item appended."""
    return items + [item.strip()]

def format_list(items):
    """Return numbered shopping lines."""
    formatted = []
    index = 1
    for item in items:
        formatted.append(f"{index}. {item}")
        index += 1
    return formatted

def main():
    items = [item.strip() for item in input("Items: ").split(",") if item.strip()]
    print("\n".join(format_list(items)))

if __name__ == "__main__":
    main()
