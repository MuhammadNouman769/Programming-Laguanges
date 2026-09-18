"""Mini project: create a reusable profile summary."""


def profile_summary(name, age, city):
    """Return a one-line profile summary."""
    return f"{name} is {age} years old and lives in {city}."


def main():
    name = input("Name: ")
    age = int(input("Age: "))
    city = input("City: ")
    print(profile_summary(name, age, city))


if __name__ == "__main__":
    main()
