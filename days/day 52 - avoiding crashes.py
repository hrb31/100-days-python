import os, time

debugMode = False
orders = []

try:
  with open('orders.txt','r') as f:
    orders = eval(f.read())
except Exception:
  print("ERROR: Unable to load")
  if debugMode:
    print(traceback)

## pizza prices
small = 10
medium = 15
large = 20
price = 0 


def add(name, size, quantity, price):
  order = ["Name: " + str(name),"Size: " + str(size), "Quantity: " + str(quantity), "Price: " + str(price)]
  orders.append(order)

def view():
  for order in orders:
    print(order, end="\n")

## subroutines could have had more lines of code instead of putting certain lines of code under the while loop


while True:
  print("1. Add order")
  print("2. View orders")
  choice = int(input("Enter choice: "))
  print()
  time.sleep(1)
  os.system("clear")
  
  if choice == 1:
    name = input("Enter name: ")
    
    size = input("Enter pizza size: ")
    if size.lower()[0] == "s":
      size = "small"
      price = small
    elif size.lower()[0] == "m":
      size = "medium"
      price = medium
    elif size.lower()[0] == "l":
      size = "large"
      price = large

    quantity = 0
    integer = False
    while not integer:
      try:
        quantity = int(input("Enter quantity: "))
        quantity = int(quantity)
        integer = True
      except Exception:
        print("ERROR: Please enter an integer")
        continue

    price = price * quantity
    print("Price: £" + str(price))
    add(name, size, quantity, price)
    time.sleep(1)

  elif choice == 2:
    view()
    time.sleep(1)

  else:
    with open('orders.txt','w') as f:
      f.write(str(orders))
    break

  again = input("Again? (y/n): ")
  if again.lower()[0] == "y":
    time.sleep(1)
    os.system("clear")
    continue
  else:
    with open('orders.txt','w') as f:
      f.write(str(orders))
    break


