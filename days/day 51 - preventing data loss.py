import os
import time

list = []

with open('todo.txt', 'r') as f:
  list = eval(f.read())

def save():
  with open('todo.txt', 'w') as f:
    f.write(str(list))

def add():
  task = input("Enter task to be done: ")
  date = input("Enter date due by: ")
  priority = input("Enter priority (high/medium/low): ")
  arr = [task,date,priority]
  list.append(arr)
  print("Task added.")

def view(choice):
  ## all
  if choice.lower()[0] == "a":
    print("All tasks:")
    for row in list:
      print(f"Task: {row[0]}\nDate Due: {row[1]}\nPriority: {row[2]}")
      print()
  ## priority
  else:
    priority = input("Enter search priority (high/medium/low): ")
    print(f"\n{priority.capitalize()} priority tasks:\n")
    for row in list:
      if row[2].lower() == priority.lower():
        print(f"Task: {row[0]}\nDate Due: {row[1]}")
        print()

def remove(task):
  for row in list:
    if row[0].lower() == task.lower():
      list.remove(row)
      print("Task removed.")
      return
  print("Task not found.")

def edit(task):
  for row in list:
    if row[0].lower() == task.lower():
      task = input("Change task, or type no if you don't want to change: ")
      if task.lower() != "no":
        row[0] = task
      date = input("Change date, or type no if you don't want to change: ")
      if date.lower() != "no":
        row[1] = date
      priority = input("Change priority, or type no if you don't want to change: ")
      if priority.lower() != "no":
        row[2] = priority
      print("Task edited.")

while True:
  print("Life Organizer")
  choice = input("""Welcome to the life organizer. Do you want to add, view, edit or remove a to do?: """)
  if choice.lower() == "add":
    add()
  elif choice.lower() == "view":
    choice = input("Do you want to view all tasks or search by priority?: ")
    view(choice)
  elif choice.lower() == "remove":
    task = input("Enter task to be removed: ")
    remove(task)
  elif choice.lower() == "edit":
    task = input("Enter task to be edited: ")
    edit(task)
  else:
    print("Invalid choice.")

  save()
  
  again = input("Do you want to see the menu again or quit?: ")
  
  if again.lower() == "quit":
    break
  else:
    time.sleep(1)
    os.system('clear')
    continue

  
