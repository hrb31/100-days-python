f = open("high.score", "r")
list = []
while True:
  line = f.readline().strip()
  score = line[3:]
  initials = line[:3]
  if line == "":
    break
  list.append([initials, int(score)])

highest = 0
name = ""
for pair in list:
  if pair[1] > highest:
    highest = pair[1]
    name = pair[0]
  
print(f"The highest score is {name} with score {str(highest)}")
