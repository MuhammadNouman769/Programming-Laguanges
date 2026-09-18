"""Mini project: summarize converted measurements."""

def convert(values, factor=1.0):
    """Convert numeric text values by factor."""
    return [float(value) * factor for value in values]

def summary(values):
    """Return count and total."""
    count = 0
    total = 0
    for value in values:
        count += 1
        total += value
    return {"count": count, "total": total}

def main():
    values = convert(input("Measurements: ").split())
    print(summary(values))

if __name__ == "__main__":
    main()
