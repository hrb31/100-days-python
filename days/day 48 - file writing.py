f = open("high.scores.txt", "a+")

running = True
while running:
  initials = input("Enter your 3 letter initials: ")
  score = int(input("Enter your score out of 100,000: "))
  f.write(initials + " " + str(score) + "\n")
  
  print("\nAdded to high score table.")
  again = input("Add another? y/n ")
  
  running = True if again == "y" else False

f.close()
    
