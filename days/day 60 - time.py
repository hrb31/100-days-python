## abs() function is used to get the absolute value of a number (positive value in this case)
## functions:
## datetime.date.today() - returns the current date
## datetime.date(year, month, day) - returns a date object
## datetime.timedelta(days=days) - returns a timedelta object (can be used to add or subtract days from a date)
## .days - returns the number of days in a timedelta object 
## timedelta - difference between two dates
## timedelta object = a data type that represents a duration, the difference between two dates or times



import datetime

today = datetime.date.today()

name = input("Name of event: ")
date = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

event = datetime.date(year, month, date)

delta = event - today

if event == today:
  print(f"Today is {name}!")
elif event > today:
  print(f"{delta.days} days left until {name}!")
else:
  print(f"{name} was {abs(delta.days)} days ago!")



