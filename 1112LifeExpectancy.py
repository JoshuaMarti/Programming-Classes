#Loading In Data
isFirstLine = True
entities = []
years = []
lifeExpectancies = []
with open("life-expectancy.csv") as inputFile:
    for line in inputFile:
        if isFirstLine:
            print("Loading Data")
            isFirstLine = False
        else:
            ingest = line.split(",")
            entities.append(ingest[0])
            years.append(int(ingest[2]))
            lifeExpectancies.append(float(ingest[3]))
print("Data Loaded Successfully")

print("\n\n")
#Max Life Expectancy
maxLifeExpectancy = 0
maxLifeExpectancySpot = 0
for spot in range(len(lifeExpectancies)):
    if lifeExpectancies[spot] > maxLifeExpectancy:
        maxLifeExpectancy = lifeExpectancies[spot]
        maxLifeExpectancySpot = spot
print(f"The overall max life expectancy is {maxLifeExpectancy} years from {entities[maxLifeExpectancySpot]} in {years[maxLifeExpectancySpot]}")

#Min Life Expectancy
minLifeExpectancy = maxLifeExpectancy
minLESpot = 0
for spot in range(len(lifeExpectancies)):
    if lifeExpectancies[spot] < minLifeExpectancy:
        minLifeExpectancy = lifeExpectancies[spot]
        minLESpot = spot
print(f"The overall min life expectancy is {minLifeExpectancy} years from {entities[minLESpot]} in {years[minLESpot]}")
