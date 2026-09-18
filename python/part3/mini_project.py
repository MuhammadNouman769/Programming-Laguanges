"""Mini project: summarize scores with small functions."""


def normalize(scores, maximum=100):
    """Return scores as fractions of maximum."""
    return [score / maximum for score in scores]


def report(scores):
    """Return count, highest score, and average score."""
    if not scores:
        return {"count": 0, "highest": 0, "average": 0}
    count = 0
    total = 0
    highest = scores[0]
    for score in scores:
        count += 1
        total += score
        if score > highest:
            highest = score
    return {"count": count, "highest": highest, "average": total / count}


def main():
    scores = [float(value) for value in input("Scores: ").split()]
    print(report(scores))


if __name__ == "__main__":
    main()
