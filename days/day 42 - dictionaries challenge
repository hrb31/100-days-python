from colorama import Fore


mokeDict = {"name": None, 
            "type": None, 
            "specialMove": None, 
            "startingHP": None, 
            "startingMP": None
           }

keys = mokeDict.keys()

for key in keys:
  mokeDict[key] = input(f"Enter your beast's {key}: ")

if mokeDict["type"] == "fire":
  colour = Fore.RED
elif mokeDict["type"] == "water":
  colour = Fore.BLUE
elif mokeDict["type"] == "earth":
  colour = Fore.GREEN
elif mokeDict["type"] == "spirit":
  colour = Fore.CYAN
elif mokeDict["type"] == "teg":
  colour = Fore.MAGENTA
else:
  colour = Fore.WHITE

print(colour + f"Your beast is called {mokeDict['name']}. Its beast type is {mokeDict['type']}. It has {mokeDict['startingHP']} HP and {mokeDict['startingMP']} MP. It's special move is {mokeDict['specialMove']}.")
