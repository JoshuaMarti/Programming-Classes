#Wordle Project, Josh Martinez
import random

words = ["academy", "airport", "analyst", "anxiety", "anxious", "assault", "auction", "battery", "binding", "billion", "boredom", "brother", "burning", "cabinet", "caliber", "capital", "capitol", "capture", "caution", "central", "centric", "chamber", "chapter", "charity", "climate", "chronic", "circuit", "clothes", "combine", "complex", "compete", "conduct", "consent", "context", "convert", "counsel", "council", "culture", "desktop", "develop", "destroy", "dispute", "diverse", "divided", "dynamic", "economy", "elderly", "enhance", "explain", "explore", "express", "factory", "faculty", "feature", "federal", "fiction", "fifteen", "sixteen", "forward", "founder", "freedom", "gateway", "gigabit", "highway", "history", "holding", "housing", "hundred", "husband", "imaging", "improve", "include", "inquiry", "interim", "justify", "keeping", "killing", "kingdom", "kitchen", "landing", "leisure", "leading", "liberal", "logical", "loyalty", "liberty", "machine", "married", "massive", "measure", "medical", "mention", "message", "massage", "mission", "mistake", "monitor", "monthly", "musical", "mystery", "natural", "nervous", "network", "neutral", "nuclear", "nursing", "obvious", "offense", "offence", "officer", "operate", "opinion", "optical", "organic", "outlook", "pacific", "painted", "package", "passage", "payment", "passive", "passion", "payable", "payment", "patient", "pension", "penalty", "pending", "perfect", "phoenix", "pioneer", "premium", "printer", "privacy", "private", "produce", "program", "promise", "promote", "project", "publish", "protect", "phished", "quality", "quantum", "radical", "rapture", "railway", "reality", "realize", "receipt", "recover", "repaint", "related", "release", "removal", "removed", "reserve", "respect", "resolve", "rollout", "require", "retired", "revenue", "satisfy", "satiate", "seventh", "service", "silicon", "skilled", "species", "sponsor", "storage", "station", "surplus", "survive", "suspect", "sustain", "teacher", "telecom", "tension", "theater", "therapy", "thereby", "therein", "thought", "through", "totally", "touched", "traffic", "trouble", "uniform", "unknown", "unusual", "utility", "vehicle", "venture", "version", "veteran", "virtues", "village", "violent", "wanting", "warning", "warrant", "waiting", "webcast", "website", "wedding", "weekend", "welfare", "western", "working", "yeeting", "yoinked", "xeroxed", "cyclops", "zooting", "quoting"]
#words = ["trouble", "uniform"] #Debug
guess = ""
#inWord = 0
print("Welcome to the Word Guessing Game! Guess \"quit\" to quit at any time.")
while guess != "quit":
    word = random.choice(words)
    #word = "wedding" #Debug
    guessCount = 0
    print("Your hint is", end="")
    for spot in range(len(word)):
        print(" _", end="")
    while guess != "quit" and guess != word:


        guess = input("\nMake a guess: ").lower()
        if guess != word and len(guess) == len(word):

            print(f"\nYour hint is", end="")
            for spot in range(len(word)):
                #print(inWord)
                if word[spot] == guess[spot]:
                    print(f" {guess[spot].upper()}", end="")
                
                else:
                    inWord = 0
                    for wordSpot in range(len(word)):
                        if guess[spot] == word[wordSpot]:
                            inWord = 1
                    if inWord == 1:
                        print(f" {guess[spot]}", end="")
                    else: print(" _", end="")





        elif guess != "quit": print("\nPlease make a guess of the correct length.")
        guessCount = guessCount + 1 
    if guess == word:
        guess = input(f"\nCongratulations, you won in {guessCount} guesses! Type \"quit\" to exit, or press Enter to play again: ").lower()

