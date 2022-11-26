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
option = ""

while option != "quit":
    option = input("\nWould you like to examine a YEAR, a COUNTRY, or QUIT? ").lower()
    while option != "quit" and option != "country" and option != "year":
        option = input("Would you like to examine a YEAR, a COUNTRY, or QUIT? ").lower()
    #Evaluate Year
    if option == "year":
        year = int(input("Enter the year you would like to examine: "))
        if year not in years:
            print(f"Error. No data available for {year}")
        else:
            print(f"\nFor {year}:")
            #Max Life Expectancy
            maxLifeExpectancy = 0
            maxLifeExpectancySpot = 0
            for spot in range(len(lifeExpectancies)):
                if year == years[spot]:
                    if lifeExpectancies[spot] > maxLifeExpectancy:
                        maxLifeExpectancy = lifeExpectancies[spot]
                        maxLifeExpectancySpot = spot

            #Min Life Expectancy and Average Life Expectancy
            minLifeExpectancy = maxLifeExpectancy
            minLESpot = 0
            average = 0
            averageDivider = 0
            for spot in range(len(lifeExpectancies)):
                if year == years[spot]:
                    average = average + lifeExpectancies[spot]
                    averageDivider = averageDivider + 1
                    if lifeExpectancies[spot] < minLifeExpectancy:
                        minLifeExpectancy = lifeExpectancies[spot]
                        minLESpot = spot
            average = average / averageDivider
            print(f"The average life expectancy across all countries was {average:,.2f}")
            print(f"The max life expectancy was {maxLifeExpectancy:,.2f} in {entities[maxLifeExpectancySpot]}")
            print(f"The min life expectancy was {minLifeExpectancy:,.2f} in {entities[minLESpot]}")
 #Evaluate Country
    if option == "country":
        country = (input("Enter the country you would like to examine: ")).title()
        if country not in entities:
            print(f"Error. No data available for {country}")
        else:
            print(f"\nFor {country}:")
            #Max Life Expectancy
            maxLifeExpectancy = 0
            maxLifeExpectancySpot = 0
            for spot in range(len(lifeExpectancies)):
                if country == entities[spot]:
                    if lifeExpectancies[spot] > maxLifeExpectancy:
                        maxLifeExpectancy = lifeExpectancies[spot]
                        maxLifeExpectancySpot = spot

            #Min Life Expectancy and Average Life Expectancy
            minLifeExpectancy = maxLifeExpectancy
            minLESpot = 0
            average = 0
            averageDivider = 0
            for spot in range(len(lifeExpectancies)):
                if country == entities[spot]:
                    average = average + lifeExpectancies[spot]
                    averageDivider = averageDivider + 1
                    if lifeExpectancies[spot] < minLifeExpectancy:
                        minLifeExpectancy = lifeExpectancies[spot]
                        minLESpot = spot
            average = average / averageDivider
            print(f"The average life expectancy across all years was {average:,.2f}")
            print(f"The max life expectancy was {maxLifeExpectancy:,.2f} in {years[maxLifeExpectancySpot]}")
            print(f"The min life expectancy was {minLifeExpectancy:,.2f} in {years[minLESpot]}")
                    

