import random

numList = []

while len(numList) < 8:
  num = random.randint(0,90)
  if num not in numList:
    numList.append(num)

numList.sort()

row1 = [numList[0], numList[1], numList[2]]
row2 = [numList[3], "BINGO", numList[4]]
row3 = [numList[5], numList[6], numList[7]]

bingoCard = [row1, row2, row3]

print("Bingo Card Generator")
print()

for row in bingoCard:
  if row[1] == "BINGO":
    print("-------------------")
    print(f"{row[0]:<4} | {row[1]} | {row[2]:>4}")
    print("-------------------")
  else:
    print(f"{row[0]:<4} | {row[1]:^4}  | {row[2]:>4}")
  
