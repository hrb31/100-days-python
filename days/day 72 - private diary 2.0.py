from replit import db
from getpass import getpass
import datetime
import hashlib
import os
import secrets
import time


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def hash_password(password, salt):
  password_and_salt = f"{password}{salt}"
  return hashlib.sha256(password_and_salt.encode()).hexdigest()


def create_account():
  clear_screen()
  print("=== First-Time Account Setup ===")
  print()

  username = input("Create a username: ").strip()
  password = getpass("Create a password: ")

  salt = secrets.token_hex(16)
  password_hash = hash_password(password, salt)

  db["account"] = {
    "username": username,
    "password": password_hash,
    "salt": salt
  }

  print("\nAccount created successfully!")
  time.sleep(2)


def login():
  clear_screen()
  print("=== Private Diary Login ===")
  print()

  username = input("Username: ").strip()
  password = getpass("Password: ")

  account = db["account"]
  password_hash = hash_password(password, account["salt"])

  if username == account["username"] and password_hash == account["password"]:
    print("\nLogin successful!")
    time.sleep(1)
    return True

  print("\nIncorrect username or password. Please try again.")
  time.sleep(2)
  return False


def add_entry():
  clear_screen()
  print("=== Add Diary Entry ===")
  print()

  entry = input("> ")
  timestamp = datetime.datetime.now()
  db[f"entry{timestamp}"] = entry

  print("\nSaved successfully!")
  time.sleep(2)


def view_entries():
  clear_screen()
  entries = list(db.prefix("entry"))
  entries = entries[::-1]

  if not entries:
    print("There are no diary entries yet.")
    time.sleep(2)
    return

  for position, entry_key in enumerate(entries):
    clear_screen()
    print(f"=== Diary Entry: {entry_key[5:]} ===")
    print()
    print(db[entry_key])

    if position < len(entries) - 1:
      print()
      choice = input("View the next entry? (y/n): ").strip().lower()
      if choice != "y":
        break
    else:
      input("\nNo more entries. Press Enter to return to the menu...")


def diary_menu():
  while True:
    clear_screen()
    print("=== Private Diary ===")
    print()
    print("1. Add an entry")
    print("2. View entries")
    print("3. Exit")
    print()

    choice = input("Choose an option: ").strip()

    if choice == "1":
      add_entry()
    elif choice == "2":
      view_entries()
    elif choice == "3":
      clear_screen()
      print("Goodbye!")
      break
    else:
      print("\nInvalid option. Please choose 1, 2, or 3.")
      time.sleep(2)


def main():
  keys = db.keys()

  if "account" not in keys:
    create_account()

  while not login():
    pass

  diary_menu()


if __name__ == "__main__":
  main()
