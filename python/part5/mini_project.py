"""Mini project: track completed study topics."""


def completed_topics(topics, completed=None):
    """Return a numbered study summary.

    When completed topics are supplied, each item is marked as complete or
    still pending. Without a completed list, the original numbered output is
    preserved for simple topic lists.
    """
    clean_topics = [topic.strip() for topic in topics if topic and topic.strip()]
    completed_topics_set = {topic.strip() for topic in (completed or []) if topic and topic.strip()}

    numbered = []
    for index, topic in enumerate(clean_topics, start=1):
        if completed is None:
            numbered.append(f"{index}. {topic}")
        else:
            status = "✅" if topic in completed_topics_set else "⏳"
            numbered.append(f"{index}. {topic} {status}")
    return numbered


def main():
    topics = [topic.strip() for topic in input("Topics: ").split(",") if topic.strip()]
    completed_input = input("Completed (optional): ").strip()
    completed = [topic.strip() for topic in completed_input.split(",") if topic.strip()] if completed_input else None

    summary = completed_topics(topics, completed)
    if not summary:
        print("No topics added.")
        return

    print("\n".join(summary))
    if completed is not None:
        print(f"\nCompleted: {len(set(completed))}/{len(topics)}")


if __name__ == "__main__":
    main()
