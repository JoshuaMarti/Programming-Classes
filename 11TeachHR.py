names = []
titles = []

with open("hr_system.txt") as inputFile:
    for line in inputFile:
        ingest = line.split()
        names.append(ingest[0])
        titles.append(ingest[2])

for spot in range(len(titles)):
    print(f"Name: {names[spot]}, Title: {titles[spot]}")