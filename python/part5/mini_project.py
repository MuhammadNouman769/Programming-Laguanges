"""Mini project: track completed study topics."""


def completed_topics(topics):
    """Return a numbered study summary."""
    return [f"{index}. {topic}" for index, topic in enumerate(topics, 1)]


def main():
    print("\n".join(completed_topics(input("Topics: ").split(","))))


if __name__ == "__main__":
    main()
