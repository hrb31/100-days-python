## db feature replit exclusive
## db["key"] = "value" to set a key
## db["key"] to get a key's value
## del db["key"] to delete a key
## db.keys() to get all keys (print(list(db.keys())))
## matches = db.prefix("key") to get all keys that start with "key"


from replit import db
import os, time, datetime

def add():
  time.sleep(1)
  os.system('clear')
  tweet = input("Enter your tweet: ")
  timestamp = datetime.datetime.now()
  db[f"tweet{timestamp}"] = tweet
  print("Tweet added!")
  time.sleep(1)
  os.system('clear')
  time.sleep(1)

def view():
  time.sleep(1)
  os.system('clear')
  keys = list(db.prefix("tweet"))
  keys = keys[::-1]
  i = 0
  print("Tweets: \n")
  for key in keys:
    time.sleep(0.3)
    print(db[key])
    i += 1
    if i % 10 == 0:
      again = input("Show 10 more? (y/n) ")
      time.sleep(0.5)
      if again == "n":
        os.system('clear')
        break
      else:
        os.system('clear')
        continue

  print()
  time.sleep(1)
  print("End of tweets.")
  time.sleep(1.5)
  os.system('clear')


while True:

  print("Welcome to the Twitter Clone!")
  menu = int(input("1: Add, 2: View, 3: Exit > "))
  if menu == 1:
    add()
  elif menu == 2:
    view()
  elif menu == 3:
    exit()
  else:
    print("Invalid option. Please try again.")
    time.sleep(0.5)
    os.system('clear')
    continue

  
  
      




