"""Mini project: process jobs lazily."""


def pending_jobs(jobs):
    """Yield jobs in execution order."""
    yield from jobs


def process(jobs):
    """Return a list of completed job labels."""
    return [f"done: {job}" for job in pending_jobs(jobs)]


def main():
    print(process(input("Jobs: ").split()))


if __name__ == "__main__":
    main()
