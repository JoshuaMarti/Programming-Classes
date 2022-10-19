#20221019 Joshua Martinez
age_first = int(input("What is the age of the first rider in years? "))
height_first = int(input("What is the height of the first rider in inches? "))
if height_first < 36: can_ride = "oneCan't"
else:
    second = input("Is there a second rider? (y/n): ").lower()
    while second != "y" and second != "n":
        second = input("Is there a second rider? (y/n): ").lower()

    if second == "n":
        if age_first >= 18 and height_first >= 62: can_ride = "oneRider"
        else: can_ride = "noOneRider"

    if second == "y":
     age_second = int(input("What is the age of the second rider? "))
     height_second = int(input("What is the height of the second rider? "))
    if height_second < 36 and age_first >= 18 and height_first >= 62: can_ride = "secondCan't"
    elif age_first >=18 or age_second >= 18: can_ride = "twoRider"
    else: can_ride = "neitherCan"



if can_ride == "oneCan't" or can_ride == "noOneRider": print("Sorry, you can't ride.")
elif can_ride == "oneRider": print("Welcome aboard! You can ride.")
elif can_ride == "secondCan't": print("Sorry, only the first of you can ride.")
elif can_ride == "twoRider": print("Welcome aboard! You can both ride.")
elif can_ride == "neitherCan": print("Sorry, neither of you can ride.")


    