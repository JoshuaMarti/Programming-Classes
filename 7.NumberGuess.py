#221026
import random

exit = False
guess = int(0)
guess_Count = 0
while not exit:
    print("You can exit the program at any time by guessing \"exit\"")
    magic_Number = random.randint(1,1000)
    while guess != magic_Number and guess != -1:
        guess = input("Guess a positive number: ")
        if guess == "exit":
            guess = -1
            exit = True
        else:
            guess = int(guess)
            guess_Count = guess_Count + 1
            if guess == magic_Number:
                print(f"Congratulations, you guessed it in {guess_Count} tries!")
                playagain = input("If you would like to quit, type \"exit\", otherwise press enter to play again")
                if playagain == "exit": exit = True
            elif guess > magic_Number:
                print("Lower")
            elif guess < magic_Number:
                print("Higher")
            else:
                print("Error. You should never see this message.")
print("Thank you for playing!")