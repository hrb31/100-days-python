import os,time

debugMode = False
inventory = []

try:
  with open('inventory.txt','r') as f:
    orders = eval(f.read())
except Exception:
  print("ERROR: Unable to load")
  if debugMode:
    print(traceback)

def add(item):
  item = item.capitalize()
  inventory.append(item)
  print(f"{item} added to inventory")

def remove(item):
  item = item.capitalize()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} removed from inventory")
  else:
    print(f"{item} not in inventory")

def view():
  seen = []
  print("Inventory:")
  print()
  for item in inventory:
    if item not in seen:
      print(f"{item} ({inventory.count(item)})")
      seen.append(item)

while True:
  os.system('clear')
  print("RPG Inventory")
  choice = int(input("1: Add 2: Remove 3: View 4: Exit > "))
  time.sleep(1)
  os.system('clear')
  if choice == 1:
    item = input("What item do you want to add? ")
    add(item)
  elif choice == 2:
    item = input("What item do you want to remove? ")
    remove(item)
  elif choice == 3:
    view()
  elif choice == 4:
    print("Goodbye")
    break
  else:
     print("Invalid choice")
     continue
    
  time.sleep(1)  
  
  with open('inventory.txt','w') as f:
    f.write(str(inventory))
    
