from replit import db
import os, time, datetime

timestamp = datetime.datetime.now()
db["password"] = "secret123"

def clear():
  os.system("clear")

def add():
  time.sleep(1)
  clear()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[f"entry{timestamp}"] = entry
  time.sleep(1)
  print("Saved successfully!")
  time.sleep(1)
  clear()

def view():
  time.sleep(1)
  clear()
  entries = list(db.prefix("entry"))
  entries =  entries[::-1]
  counter = 0
  for entry in entries:
    print(f"Diary entry for {entry[5:]}")
    print(db[entry])
    time.sleep(1)
    counter += 1
    if counter < len(entries):
      next = input("Next entry? y/n > ")
      if next == "y":
        clear()
        continue
      else:
        break
    else:
      time.sleep(1)
      print("No more entries.")
      time.sleep(1)
      clear()

  time.sleep(1)
  clear()

def menu():
  while True:
    print("1: Add 2: View 3: Exit")
    menu = int(input("> "))
    if menu == 1:
      add()
    elif menu == 2:
      view()
    elif menu == 3:
      time.sleep(0.5)
      print("Goodbye!")
      exit()
    else:
      time.sleep(1)
      print("Invalid option. Please try again.")
      time.sleep(0.5)
      os.system('clear')
      continue

while True:
  password = input("Enter password: ")
  if password == db["password"]:
    time.sleep(1)
    clear()
    menu()
  else:
    time.sleep(1)
    print("Incorrect password. Please try again.")
    time.sleep(0.5)
    clear()
