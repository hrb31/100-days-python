mokeDict = {}

def prettyPrint(dict):
  for key, value in dict.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
    print()


while True:
  mokeDetails = { 
    "type": None, 
    "specialMove": None, 
    "startingHP": None, 
    "startingMP": None
   }

  name = input("Enter your beast's name: ")
  keys = mokeDetails.keys()
  for key in keys:
    mokeDetails[key] = input(f"Enter your beast's {key}: ")
  mokeDict[name] = mokeDetails

  
  again = input("Again? y/n: ") 
  
  if again == "n":
    break
  else:
    continue

print()
prettyPrint(mokeDict)
