"""Mini project: produce a student result report."""


def result(name, marks):
    """Return a compact result record."""
    average = sum(marks) / len(marks) if marks else 0
    status = "pass" if average >= 50 else "fail"
    return {"name": name, "average": average, "status": status}


def main():
    marks = [float(value) for value in input("Marks: ").split()]
    print(result(input("Name: "), marks))


if __name__ == "__main__":
    main()
