"""Mini project: format a contact card."""

def contact_card(name, phone, email):
    """Return a readable contact card."""
    return f"{name.strip().title()} | {phone.strip()} | {email.strip().lower()}"

def main():
    print(contact_card(input("Name: "), input("Phone: "), input("Email: ")))

if __name__ == "__main__":
    main()
