"""Mini project: create an interview revision scorecard."""

def score(topics, completed):
    """Return completion count and percentage."""
    total = len(topics)
    count = sum(topic in completed for topic in topics)
    return {"completed": count, "total": total, "percent": count / total * 100 if total else 0}

def main():
    topics = input("Topics: ").split(",")
    completed = set(input("Completed: ").split(","))
    print(score(topics, completed))

if __name__ == "__main__":
    main()
