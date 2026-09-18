"""Practice string counting."""

def vowel_count(text):
    """Count vowels without changing the original text."""
    return sum(character.lower() in "aeiou" for character in text)

def main():
    print(vowel_count(input("Text: ")))

if __name__ == "__main__":
    main()
