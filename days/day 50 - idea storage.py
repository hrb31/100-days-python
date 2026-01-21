import random

## os and time could be useful in this project if developed further

print("Idea Storage")
print()

with open("ideas.txt", "w") as f:
  f.write("A fitness app where workouts are themed around movie scenes")

def menu():
  choice = input("Add an idea or see a random idea? (a/r): ")
  print()
  
  if choice.lower() == "a":
    idea = input("Enter your idea: ")
    with open("ideas.txt", "a") as f:
      f.write("\n" + idea)

    print()
    print("Idea added!")
    print()
    

  elif choice.lower() == "r":
    with open("ideas.txt", "r") as f:
      ideas = f.readlines()
      print(random.choice(ideas).strip())
      print()

  else:
    print("Invalid input")


while True:
   menu()


      
     
     
  
