print("Website Rating")
name = input("Enter website name: ")
url = input("Enter website URL: ")
description = input("Enter website description: ")
rating = input("Enter website rating in stars out of 5: ")

webDict = {"name": name, "url": url, "description": description, "rating": rating}

for name, value in webDict.items():
  if name != "rating":
    print(f"{name}:{value}", end=", ")
  else:
    print(f"{name}:{value}")


## creating dictionary before - check if it works idk
websiteDict = {"name": "", "url": "", "description": "", "rating": ""}

for name in websiteDict.keys():
  websiteDict[name] = input(f"Enter website {name}: ")

print()
for name, value in websiteDict.items():
  print(f"{name}: {value}")
