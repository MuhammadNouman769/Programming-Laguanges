"""Practice key functions with sorted."""


def sort_by_length(words):
    """Return words ordered by length."""
    ordered = []
    for word in words:
        word_size = 0
        for _character in word:
            word_size += 1
        position = 0
        ordered_size = 0
        for _item in ordered:
            ordered_size += 1
        while position < ordered_size:
            existing_size = 0
            for _character in ordered[position]:
                existing_size += 1
            if existing_size > word_size:
                break
            position += 1
        ordered.insert(position, word)
    return ordered


def main():
    print(sort_by_length(input("Words: ").split()))


if __name__ == "__main__":
    main()
