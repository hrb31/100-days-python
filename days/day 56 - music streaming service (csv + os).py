import os, csv

with open("100MostStreamedSongs.csv", "r") as file:
  reader = csv.DictReader(file)
  
  for row in reader:
    files = os.listdir()
    if row['Artist(s)'] not in files:
      os.mkdir(f"{row['Artist(s)']}")
    filename = os.path.join(f"{row['Artist(s)']}/",f"{row['Song']}.txt")
    with open(filename, "w") as file:
      pass

