"""Practice a leap-year condition."""


def is_leap_year(year):
    """Return whether year follows Gregorian leap-year rules."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    print(is_leap_year(int(input("Year: "))))


if __name__ == "__main__":
    main()
