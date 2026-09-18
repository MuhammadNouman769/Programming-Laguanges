"""Practice range creation."""

def make_range(start, stop, step=1):
    """Return a list made from range arguments."""
    return list(range(start, stop, step))

def main():
    print(make_range(int(input("Start: ")), int(input("Stop: "))))

if __name__ == "__main__":
    main()
