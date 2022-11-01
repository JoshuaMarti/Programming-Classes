num = 0
while num <= 0:
    num = int(input("Please enter a positive number: "))
    if num <= 0:
        print("Sorry, try again.")
can_have_candy = False
while not can_have_candy:
    var = input("May I please have a piece of candy? ")
    if var.lower() == "yes":
        can_have_candy = True
print("Thank you =D")