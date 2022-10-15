#Copyright 2022, Joshua Martinez
#Intended to run in Python
print("Welcome to CYoA Delta Lite!")
start_trigger = input("\nPress Enter to Start")
character = input("Please type a name for a character: ").title()
morality = 0

print ("\n\n\n\n\n\n\n\n\n\nLoading...\n")
print("\n\n\nIt's 2025. After teetering on the brink of nuclear conflict, the Ukra-Russio War has come to a close")
print(f"and it has been a calm couple years. You and {character} are out for a stroll when you peek inside a pastry shop and find it empty.")
choiceA = input("\nDo you LOOK inside, GO in the shop, or KEEP walking?\n   ").lower()
while choiceA != "look" and choiceA != "go" and choiceA != "keep":
    choiceA = input("LOOK inside, GO inside, or KEEP walking?\n   ").lower()
if choiceA == "look":
    print("\nAs you look around through the large window, you find it is indeed empty. Some personal belongings are on the tables, but nobody seems to be around.")
    choiceA = input("\nDo you GO in the shop, or KEEP walking?\n   ").lower()
    while choiceA != "go" and choiceA != "keep":
        choiceA = input("GO inside, or KEEP walking?\n   ").lower()
if choiceA == "go":
    print("\nIt's like everyone got up and ran out. There's a laptop and phone at one of the tables, jackets on a few chairs, and")
    print(f"Much to your surprise, there are piles of clothes scattered around. \"This is giving me the creeps\" comments {character}.")
    choiceA = input("\nDo you STEAL some of the abandoned belongings, EAT some pastries, or leave and KEEP walking?\n   ").lower()
    while choiceA != "steal" and choiceA != "keep" and choiceA != "eat":
        choiceA = input("STEAL belongings, EAT pastries, or KEEP walking?\n   ").lower()
    if choiceA == "steal":
        print(f"\nYou glance around one more time, and slip a few phones and a wallet into your pockets before you leave. {character} looks at you disapprovingly, but he doesn't stop you.")
        print("Satisfied, you declare \"Let's get out of here \", to which Andy agrees")
        choiceA = "keep"
        morality = morality-1
    elif choiceA == "eat":
        print("\nYour stomach rumbles. Eying the pastries, you snatch one up and start munching.")
        choiceA = "keep"
        choiceB = input("\nDo you PAY for the pastry, or LEAVE without paying?\n   ").lower()
        while choiceB != "pay" and choiceA != "leave":
            choiceB = input("LEAVE without paying, or PAY for the pastry?\n   ").lower()
        if choiceB == "pay":
            print(f"\nYou pull out your wallet, look at the menu, and leave enough cash for your pastry on the counter with a note. {character} does the same.")
            morality = morality+1
        elif choiceB == "leave":
            morality = morality-1
            print(f"Satisfied, you turn to leave. {character} looks on disapprovingly as they pull out their wallet and leave enough cash to cover both of your pastrys on the counter.")
if choiceA == "keep":
    print(f"\nYou and {character} continue walking along the deserted street. As you come around the corner to an intersection, you see two cars crashed in the middle of it.")

