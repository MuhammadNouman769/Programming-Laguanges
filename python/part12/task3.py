"""Practice set uniqueness."""

def unique(items):
    """Return sorted unique items."""
    unique_items = []
    for item in items:
        found = False
        for saved_item in unique_items:
            if saved_item == item:
                found = True
                break
        if not found:
            unique_items.append(item)
    index = 1
    item_count = 0
    for _item in unique_items:
        item_count += 1
    while index < item_count:
        current = unique_items[index]
        previous = index - 1
        while previous >= 0 and unique_items[previous] > current:
            unique_items[previous + 1] = unique_items[previous]
            previous -= 1
        unique_items[previous + 1] = current
        index += 1
    return unique_items

def main():
    print(unique(input("Items: ").split()))

if __name__ == "__main__":
    main()
