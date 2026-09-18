"""Practice an eligibility condition."""

def eligible(age, minimum=18):
    """Return whether age meets minimum."""
    return age >= minimum

def main():
    print(eligible(int(input("Age: "))))

if __name__ == "__main__":
    main()
