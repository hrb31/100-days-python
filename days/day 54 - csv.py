import csv 

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    add = float(row["Cost"]) * float(row["Quantity"])
    total += add

print("Shop Tracker")
print()
print(f"Your shop took £{round(total,2)} pounds today")
