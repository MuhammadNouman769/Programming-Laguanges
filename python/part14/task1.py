"""Practice range creation."""

def make_range(start, stop, step=1):
    """Return a list made from range arguments."""
    values = []
    value = start
    if step > 0:
        while value < stop:
            values.append(value)
            value += step
    elif step < 0:
        while value > stop:
            values.append(value)
            value += step
    else:
        raise ValueError("step cannot be zero")
    return values

def main():
    print(make_range(int(input("Start: ")), int(input("Stop: "))))

if __name__ == "__main__":
    main()
