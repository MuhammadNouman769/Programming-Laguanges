"""Practice a dictionary frequency count."""

def frequencies(words):
    """Return word frequencies."""
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

def main():
    print(frequencies(input("Words: ").split()))

if __name__ == "__main__":
    main()
