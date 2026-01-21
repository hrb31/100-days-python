class character():
  name = None
  health = 100
  magicPoints = 100

  def __init__(self, name):
    self.name  = name

  def printDetails(self):
    print("Name: ", self.name)
    print("Health: ", self.health)
    print("Magic Points: ", self.magicPoints)

  def setStats(self, health, magicPoints):
    self.health = health
    self.magicPoints = magicPoints

class player(character):
  nickname = None
  lives = 3
  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def checkStatus(self):
    if self.health > 0:
      print("Player is alive")
      return True
    else:
      print("Player is dead")
      return False

  def printDetails(self):
     print("Name: ", self.name)
     print("Nickname: ", self.nickname)
     print("Health: ", self.health)
     print("Lives: ", self.lives)
     print("Magic Points: ", self.magicPoints)

bob = player("Bob")
bob.setStats(100, 100)
bob.printDetails()


class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def printDetails(self):
    print("Name: ", self.name)
    print("Type: ", self.type)
    print("Strength: ", self.strength)
    print("Health: ", self.health)


class orc(enemy):
  speed = None
  
  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def printDetails(self):
    print("Name: ", self.name)
    print("Type: ", self.type)
    print("Strength: ", self.strength)
    print("Speed: ", self.speed)

orc1 = orc(100)
orc1.printDetails()

orc2 = orc(200)
orc2.printDetails()


class vampire(enemy):
  day = None

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    if day:
      self.day = "Day"
    else:
      self.day = "Night"

  def printDetails(self):
    print("Name: ", self.name)
    print("Type: ", self.type)
    print("Strength: ", self.strength)
    print("Day/Night: ", self.day)



vampire1 = vampire(True)
vampire1.printDetails()
vampire2 = vampire(False)
vampire2.printDetails()
