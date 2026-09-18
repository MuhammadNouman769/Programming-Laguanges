"""Practice list flattening."""

def flatten(groups):
    """Return nested groups as one list."""
    return [item for group in groups for item in group]

def main():
    groups = [group.split(",") for group in input("Groups: ").split(";")]
    print(flatten(groups))

if __name__ == "__main__":
    main()
