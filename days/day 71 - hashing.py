from replit import db
from getpass import getpass
import os
import random
import time


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def new():
  clear_screen()
  print("=== Create an Account ===")
  print()
  username = input("Username: ")
  password = getpass("Password: ")
  salt = random.randint(1000,9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  db[username] = {"password": newPassword, "salt": salt}
  print("\nAccount created successfully!")
  time.sleep(2)


def login():
  clear_screen()
  print("=== Login ===")
  print()
  username = input("Username: ")
  password = getpass("Password: ")
  try:
    salt = db[username]["salt"]
    password = f"{password}{salt}"
    password = hash(password)
    if password == db[username]["password"]:
      print("\nLogin successful. Welcome!")
    else:
      print("\nIncorrect password. Please try again.")
  except KeyError:
    print("\nThat user does not exist. Please try again.")

  time.sleep(2)


def main():
  while True:
    clear_screen()
    print("=== Account System ===")
    print()
    print("1. Create a new account")
    print("2. Log in")
    print("3. Exit")
    print()

    choice = input("Choose an option: ")

    if choice == "1":
      new()
    elif choice == "2":
      login()
    elif choice == "3":
      clear_screen()
      print("Goodbye!")
      break
    else:
      print("\nInvalid option. Please choose 1, 2, or 3.")
      time.sleep(2)


if __name__ == "__main__":
  main()
