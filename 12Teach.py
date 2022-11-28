people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
names = []
ages = []
youngestSpot = 0
youngestAge = 999
for spot in range(len(people)):
    temp = people[spot].split()
    names.append(temp[0])
    ages.append(int(temp[1]))
for spot in range(len(ages)):
    if ages[spot] < youngestAge:
        youngestSpot = spot
        youngestAge = ages[spot]
print(f"The youngest person is {names[youngestSpot]} at {youngestAge} years old.")