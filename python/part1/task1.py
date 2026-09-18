"""Practice formatted output and simple functions."""


def make_greeting(name):
    """Return a friendly greeting for name."""
    return f"Hello, {name}!"


def main():
    print(make_greeting(input("Name: ")))


if __name__ == "__main__":
    main()
