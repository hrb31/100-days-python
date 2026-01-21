import random
import os
import time

def createCard():
  global bingoCard
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

def printCard():
  for row in bingoCard:
    if row[1] == "BINGO":
      print("-------------------")
      print(f"{row[0]:<4} | {row[1]} | {row[2]:>4}")
      print("-------------------")
    else:
      print(f"{row[0]:<4} | {row[1]:^4}  | {row[2]:>4}")

correct = 0

createCard()

while True:
  printCard()
  numCalled = int(input("What number was called?: "))
  
  for i in range(3):
    if numCalled in bingoCard[i]:
      index = bingoCard[i].index(numCalled)
      bingoCard[i][index] = "X"
      correct += 1  
      
  time.sleep(1)
  os.system('clear')
  print("Checking card...")
  time.sleep(1)
  os.system('clear')

  
  if correct == 8:
    print("BINGO! You have won!")
    break
        
