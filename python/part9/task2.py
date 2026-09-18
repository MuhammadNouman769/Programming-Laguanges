"""Practice grade conditions."""


def grade(mark):
    """Return a letter grade for a mark from zero to 100."""
    if not 0 <= mark <= 100:
        return "Invalid"
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def main():
    print(grade(int(input("Mark: "))))


if __name__ == "__main__":
    main()
