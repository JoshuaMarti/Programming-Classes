#Copyright 2022, Joshua Martinez
#Intended to run in Python
print("Welcome to CYoA Delta Lite!")
start_trigger = input("\nPress Enter to Start")
character = input("Please type a name for a character: ").title()
morality = 0

print ("\n\n\n\n\n\n\n\n\n\nLoading...\n")
print("\n\n\nIt's 2025. After teetering on the brink of nuclear conflict, the Ukra-Russio War has come to a close")
print(f"and it has been a calm couple years. You and {character} are out for a stroll when you peek inside a pastry shop and find it empty.")

#Begin Subsection 1
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
            print(f"\nSatisfied, you turn to leave. {character} looks on disapprovingly as they pull out their wallet and leave enough cash to cover both of your pastrys on the counter.")
if choiceA == "keep":
    print(f"\nYou and {character} continue walking along the deserted street. As you come around the corner to an intersection, you see two cars crashed in the middle of it.")

#Begin Subsection 2
choiceC = input("\nDo you RUN over to help, LOOK the situation over from afar, or IGNORE the crash and keep walking?\n   ").lower()
while choiceC != "run" and choiceC != "look" and choiceC != "ignore":
    choiceC = input("RUN over to help, LOOK the situation over from afar, or IGNORE the crash and keep walking?\n    ").lower()
if choiceC == "look":
    print("\nYou can smell the airbags, this looks like a bad one, The glass is spiderwebbed on one car, shattered on the other, its nose wedged under the belly of the first. You can't tell if anyone is still inside either of them.")
    choiceC = input("\nDo you RUN over to help, or IGNORE the crash and keep walking?\n   ").lower
    while choiceC != "run" and choiceC != "ignore":
        choiceC = input("RUN over or IGNORE the crash and keep walking?\n   ").lower()
if choiceC == "ignore":
    if morality < 0:
        print(f"\nAs you continue walking away following the curvature of the road, the crash now out of sight, {character} looks back and forth between you and the crash. Frustrated, they yell \"How can you just ignore that! First you steal, now you ignore whoever got in that crash, I'm done with you! I'm going to help\", and with that, {character} turns and bolts back.")
    else:
        print(f"As you continue walking away along the curvy road, the crash hidden behind a hill now, {character} announces \"I'm going to go help whoever was in those cars\", and they turn and jog back.")
    choiceD = input(f"\nDo you GO back to help, TRY to stop {character}, or KEEP walking?\n   ").lower()
    while choiceD != "go" and choiceD != "try" and choiceD != "keep":
        choiceD = input(f"GO back to help, TRY to stop {character}, or KEEP walking?\n   ").lower()
    if choiceD == "try":
        print(f"\nYou bolt toward {character}. You're gaining on them as you follow the curving road. Finally, the intersection with the crash is back in sight, you're almost caught up with them. You lunge, grabbing their arm. You and {character} tumble to the ground, the rough concrete scraping you both. {character} looks at you sadly, you've got them pinned now, then their arm jerks, you feel a prick and then a warmth spreading through your body. \"Im sorry\", {character} whispers as your vision blurs. They push you off of them - your strength gone - and hold you comfortingly as the whole world seems to dim, their voice sounding like they're talking through a pipe. \"You failed. But you can try again. Learn, do better\" they counsel, and then you're awake, staring at this screen, wondering what just happened.")
    elif choiceD == "keep":
        print(f"\nYou scoff and keep walking along the windy road. Thinking back, you realize things have been incredibly quiet. No birds. No breeze. No cars. Nothing except you and {character}. And now they're gone. You start feeling dizzy. You drop to your knees as your vision blurs. You struggle to stand before collapsing, your strength gone. Suddenly, you hear what sounds like the voice of {character}, distant and faint, saying \"You can learn from this. Go forward. Do better\". Your vision fades to black, and then your attention jolts back.\n\nHere you are, reading words on a screen, nothing more as you wonder what {character} meant.")
    elif choiceD == "go":
        print(f"\nYou catch up with {character}, the two of you running alongside one another. They grin at you. As you round the curve, the intersection comes in to view, but the cars are gone. Quizically, you look at {character}. \"You did it!\" they proclaim. \"You won the game\"")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
        print("\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("Thanks for playing!")
    else: print("\n\n\nError. Not sure how you got here. Error Code 071")

#Begin Subsection 3, intentional inconsistency with shop setting.
if choiceC == "run":
    print(f"\nYou and {character} bolt to the crashed cars. Together, you look inside them both, but find them empty. as though the drivers just got up and walked away. A sense of unease settles over you.")
    choiceE = input("\nDo you MOVE the cars off the road, or LET them stay?\n   ").lower()
    while choiceE != "move" and choiceE != "let":
        choiceE = input("MOVE the cars, or LET them stay in the road?\n   ").lower()
    if choiceE == "move":
        print(f"You look to {character} and nod, the understanding between you instant. Together, you each open a door of the car on the bottom car and push it backwards, guiding it off the road. You do the same to the other, leaving the road cleared. {character} smiles as you proudly. \"You did it!\" they announce. \"You won the game\"")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
        print("\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("Thanks for playing!")
    else:
        print(f"You hear a whistling from above you and look up to see a sign falling from the sky. You try to dodge it, but miss, and it thwacks you square on the noggin'. Stamped on it are the words \"This road to be extended in the future. Contact Public Works for additional information\". {character} helps you up and brushes you off.\n \"Well, you didn't lose. Congratulations, I'm proud of you\" they say, grinning")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
        print("\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("Thanks for playing!")
