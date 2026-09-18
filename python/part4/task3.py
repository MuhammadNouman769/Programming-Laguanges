"""Practice a decorator."""


def announce(function):
    """Return a wrapper that labels a function result."""
    def wrapper(*args, **kwargs):
        return f"Result: {function(*args, **kwargs)}"
    return wrapper


@announce
def add(left, right):
    return left + right


def main():
    print(add(2, 3))


if __name__ == "__main__":
    main()
