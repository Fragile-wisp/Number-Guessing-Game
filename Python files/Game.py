#Code for Number Guessing Game
import random

print("""Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have to guess it.""")

repeat = "y"
while repeat.lower() == "y":
    #Difficulty
    Difficulty = input("""Select Difficulty (just type which one):
        1.Easy (15 tries)
        2.Medium (9 tries)
        3.Hard (5 tries).\n""")
    if Difficulty.lower()=="easy":
        Attempts = 15
    elif Difficulty.lower()=="medium":
        Attempts = 9
    elif Difficulty.lower()=="hard":
        Attempts = 5
    else:
        print("Not a Valid Difficulty.\nAutomatically switching to easy")
        Attempts = 15

    #Guessing
    print("Alright let's start the game!")     
    Correct_Num = random.randint(1,100)
    for i in range(Attempts):
        try:
            guess = int(input("\nPlease enter your guess:"))
            if guess<1 or guess>100:
                print("\nNot in range! No you don't get that attempt back.")
            if guess == Correct_Num:
                print(f"\nYou have guessed the number! You guessed in {i+1} attempts.")
                break
            elif guess > Correct_Num:
                print(f"\nNumber is lower than",guess,".")
            else:
                print(f"\nNumber is greater than",guess,".")
        except ValueError:
            print("\nNot a number! You know you don't get any attempt refunds right?")
            
        if i+1 == Attempts:
            print("You have run out of attempts :(")
    
    #Try again
    repeat = input("Want to play again? (Y/N).")

if repeat.lower() != "n":
    print("\nI didn't get what you're saying. I'm just gonna end the program.\nPlease get some rest before restarting.")
    
print("""\nGame has ended. Thanks for playing!
Rerun code to restart.""")
