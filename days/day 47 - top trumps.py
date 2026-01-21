## game slightly adapted as a joke

print("Top Tegs")
print()
print("Welcome to the top tegs simulator")

tegs = {}

tegs["paseen"]= {"tegLevel": 100000000000, 
          "fortniteAbility": -1000000,
          "age" : 16,
          "height" : 180
}

tegs["zayn"] = {"tegLevel": 1000000,
        "fortniteAbility": 100,
        "age" : 7,
        "height" : 120
}

print()

running = True
while running:
  choice = int(input("Choose your card: 1. Paseen 2. Zayn\n >"))
  if choice == 1:
    choice = "paseen"
    opponent = "zayn"
  elif choice == 2:
    choice = "zayn"
    opponent = "paseen"
  else:
    print("Invalid choice. Please enter 1 or 2.")
    continue
  
  stat = int(input("Choose your stat:\n1. Teg Level\n2. Fortnite Ability\n3. Age\n4. Height\n >"))
  if stat == 1:
    stat = "tegLevel"
  elif stat == 2:
    stat = "fortniteAbility"
  elif stat == 3:
    stat = "age"
  elif stat == 4:
    stat = "height"


  print(f"{choice} has a {stat} of {tegs[choice][stat]}")
  print(f"{opponent} has a {stat} of {tegs[opponent][stat]}")

  if tegs[choice][stat] > tegs[opponent][stat]:
    print(f"{choice} wins!")
  elif tegs[choice][stat] < tegs[opponent][stat]:
    print(f"{opponent} wins!")
  else:
    print("It's a draw!")

  again = input("Would you like to play again? (y/n) > ")
  if again == "n":
    running = False
    print("Thanks for playing!")
  else:
    continue
