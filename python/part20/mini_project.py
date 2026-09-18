"""Mini project: summarize a set of numbers."""

def summarize(values):
    """Return basic comparison statistics."""
    values = list(values)
    return {"smallest": min(values), "largest": max(values), "range": max(values) - min(values)}

def main():
    print(summarize(map(int, input("Values: ").split())))

if __name__ == "__main__":
    main()
