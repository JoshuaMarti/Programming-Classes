yesNoExit = "Hold"

while yesNoExit != "exit":
    yesNoExit = input("Would you like to play again?").lower()
    if yesNoExit == "yes":
        print("Great! Let's play again.")
    elif yesNoExit == "no":
        print ("Okay, tallyho!")
    else:
        print ("Please type Yes, No, or Exit")