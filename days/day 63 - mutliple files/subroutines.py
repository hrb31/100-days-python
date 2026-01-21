from colorama import Fore
import os, time

def colourChange(letter):
  if letter.lower() == "r":
    print(Fore.RED, end="")
  elif letter.lower() == "b":
    print(Fore.BLUE, end="")
  elif letter.lower() == "g":
    print(Fore.GREEN, end="")
  elif letter.lower() == "p":
    print(Fore.MAGENTA, end="")
  elif letter.lower() == "y":
    print(Fore.YELLOW, end="")
  elif letter.lower() == " ":
    print(Fore.WHITE, end="")

def print2DArray(list):
  for row in list:
    print(row, end="\n")

def printDict2D(dict):
  for key, value in dict.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
    print()

def clear():
  os.system('clear')


def countdown():
  for i in range(10,-1,-1):
    print(i)
    time.sleep(1)

