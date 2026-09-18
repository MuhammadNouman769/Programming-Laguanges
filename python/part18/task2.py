"""Practice nested-style validation."""

def login_status(username, password):
    """Return a login result."""
    if not username:
        return "missing username"
    if not password:
        return "missing password"
    return "accepted"

def main():
    print(login_status(input("User: "), input("Password: ")))

if __name__ == "__main__":
    main()
