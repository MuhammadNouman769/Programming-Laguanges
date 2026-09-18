"""Practice dictionary access."""

def get_field(record, field, default=None):
    """Return a dictionary field or default."""
    return record.get(field, default)

def main():
    print(get_field({"name": input("Name: ")}, "name"))

if __name__ == "__main__":
    main()
