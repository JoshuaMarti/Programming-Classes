num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the second number? "))
string_1 = "not "
string_2 = "not "
string_3 = "not "
if num_1 > num_2:
    string_1 = ""
elif num_1 == num_2:
    string_2 = ""
elif num_1 < num_2:
    string_3 = ""
print(f"The first number is {string_1}greater.")
print(f"The numbers are {string_2}equal.")
print(f"The second number is {string_3}greater.")

favAnimal = (input("\nWhat is your favorite animal? "))
#print(f"Debug {favAnimal.lower()}")
if favAnimal.lower() == "capybara":
    print("That's my favorite animal too!")
else:
    print("That is not my favorite animal, but it's still a neat one!")