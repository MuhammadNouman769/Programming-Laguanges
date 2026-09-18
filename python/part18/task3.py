"""Practice score branching."""

def score_label(score):
    """Return a simple score label."""
    if score >= 80:
        return "high"
    if score >= 50:
        return "medium"
    return "low"

def main():
    print(score_label(int(input("Score: "))))

if __name__ == "__main__":
    main()
