# foods = ["Cauliflower", "Potatos", "Tomatos", "Broccoli", "Parsnips", "Wagon Wheel Pasta", "Oranges", "Bananas", "Raspberries", "Avocados"]
# for index in range(len(foods)):
#     print(f"{index}: {foods[index]}")
# foods.pop(4)
# for index in range(len(foods)):
#     print(f"{index}: {foods[index]}")
    
names = ["Chlo", "Al", "Phil", "Jenny"]
phoneNumbers = ["454-5454", "971-0304", "798-2535", "867-5309"]
for spot in range(len(names)):
    print(f"Name: {names[spot]}, Phone: {phoneNumbers[spot]}")
del names[2]
del phoneNumbers[2]

for spot in range(len(names)):
    print(f"Name: {names[spot]}, Phone: {phoneNumbers[spot]}")

names[1] = "Sara"
phoneNumbers[1] = "192-1681"

for spot in range(len(names)):
    print(f"Name: {names[spot]}, Phone: {phoneNumbers[spot]}")

names.append("Janeway")
phoneNumbers.append("622-74656")

for spot in range(len(names)):
    print(f"Name: {names[spot]}, Phone: {phoneNumbers[spot]}")