"""Mini project: validate a simple application."""

def application_status(age, income, has_id):
    """Return approval based on nested business rules."""
    if age < 18:
        return "rejected: under age"
    if income <= 0:
        return "rejected: invalid income"
    if not has_id:
        return "rejected: missing id"
    return "approved"

def main():
    print(application_status(int(input("Age: ")), float(input("Income: ")), input("Has ID? ").lower() == "yes"))

if __name__ == "__main__":
    main()
