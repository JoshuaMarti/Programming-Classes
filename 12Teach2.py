shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]
maxPrice = 0.0
maxItem = ""
for item in shopping_cart:
    item_name = item[0]
    item_price = item[1]
    print(f"Item: {item_name:10} costs ${item_price}")
    if item_price > maxPrice:
        maxPrice = item_price
        maxItem = item_name
print(f"The maximum priced item is {maxItem} at ${maxPrice}")
#Program #2:
city_data = [
'Paris France 8000000',
'London England 10000000',
'Rexburg USA 40000',
'Boise USA 220000',
'Smithfield USA 12000',
'McCall USA 5000',
]

largeCity = ""
largePop = 0
largeNation = ""
smallCity= ""
smallNation = ""
smallPop = 999999999
for spot in range(len(city_data)):
    city_list = city_data[spot].split()
    city_name = city_list[0]
    city_country = city_list[1]
    city_population = int(city_list[2])
    #print(city_population, smallPop, largePop)
    if smallPop > city_population:
        smallPop = city_population
        smallCity = city_name
        smallNation = city_country
    if largePop < city_population:
        largePop = city_population
        largeCity = city_name
        largeNation = city_country
print(f"{largeCity}, {largeNation} has the largest population with {largePop:,} people.")
print(f"{smallCity}, {smallNation} has the largest population with {smallPop:,} people.")