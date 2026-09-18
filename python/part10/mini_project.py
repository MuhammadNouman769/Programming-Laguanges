"""Mini project: summarize converted measurements."""

def convert(values, factor=1.0):
    """Convert numeric text values by factor."""
    return [float(value) * factor for value in values]

def summary(values):
    """Return count and total."""
    return {"count": len(values), "total": sum(values)}

def main():
    values = convert(input("Measurements: ").split())
    print(summary(values))

if __name__ == "__main__":
    main()
