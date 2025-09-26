import csv
import os
import getpass

USERS_FILE = "data/users.csv"

def login():
    """Login or register a user before accessing the app."""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password"])  # header

    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    with open(USERS_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return username

    # If not found, register
    print("🆕 New user, creating account...")
    with open(USERS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
    return username
