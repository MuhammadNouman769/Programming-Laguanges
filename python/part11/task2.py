"""Practice string counting."""

def vowel_count(text):
    """Count vowels without changing the original text."""
    count = 0
    for character in text:
        if character.lower() in "aeiou":
            count += 1
    return count

def main():
    print(vowel_count(input("Text: ")))

if __name__ == "__main__":
    main()
