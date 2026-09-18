"""Mini project: create an interview revision scorecard."""

def score(topics, completed):
    """Return completion count and percentage."""
    total = 0
    count = 0
    for topic in topics:
        total += 1
        if topic in completed:
            count += 1
    return {"completed": count, "total": total, "percent": count / total * 100 if total else 0}

def main():
    topics = input("Topics: ").split(",")
    completed = []
    for topic in input("Completed: ").split(","):
        already_saved = False
        for saved_topic in completed:
            if saved_topic == topic:
                already_saved = True
                break
        if not already_saved:
            completed.append(topic)
    print(score(topics, completed))

if __name__ == "__main__":
    main()
