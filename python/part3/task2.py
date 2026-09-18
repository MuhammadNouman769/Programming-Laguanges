"""Practice key functions with sorted."""


def sort_by_length(words):
    """Return words ordered by length."""
    return sorted(words, key=lambda word: len(word))


def main():
    print(sort_by_length(input("Words: ").split()))


if __name__ == "__main__":
    main()
