print("Star Wars Name Generator")
first = input("Enter your first name: ")
surname = input("Enter your surname: ")
starwarsname = first[0:3].capitalize() + surname[0:3].lower()
maiden = input("Enter your mother's maiden name: ")
city = input("Enter the city where you were born: ")
starwarsname2 = maiden[0:2].capitalize() + city[-3:].lower()
print(f"Your name is {starwarsname} {starwarsname2}")

## OR 

print("Star Wars Name Generator")
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ").split()
first = all[0].strip()
surname = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

starName = f"{first[:3].capitalize() + surname[:3].lower()} {maiden[:2].capitalize() + city[-3:].lower()}"
print(f"Your Star Wars name is {starName}")
