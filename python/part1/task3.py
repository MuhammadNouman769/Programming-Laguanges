"""Practice arithmetic with variables."""


def rectangle_area(length, width):
    """Return the area of a rectangle."""
    return length * width


def main():
    length = float(input("Length: "))
    width = float(input("Width: "))
    print(rectangle_area(length, width))


if __name__ == "__main__":
    main()
