# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Library to enable control over clearing the display
import os

# Library for pseudo random functions
import random

# testing variable as the word of the day
# wod = ""

def welcome():
    """
    Produces the welcome screen into the game including the player name input
    """
    print("""








                                   Welcome

                                      to

                                    Wordle







""")
    plr_name = input("What's your name?\n")
    return plr_name


def wod_pick():
    """
    Random selecting a 5 letter word from the word bank file
    """
    fil = open('en-us-dict.txt')
    words = fil.readlines()
    fil.close()
    return random.choice(words).strip()


def guess_input(word):
    """
    Prompts user for guess input
    """
    print(word)
    print("what is your guess?\n")
    guess = input("your guess:")
    if (guess.lower() == word):
        print(f"That's correct! {guess.upper()} is the word of the day")
    else:
        print(f"Oops! That guess is wrong. BYE!")


def main():
    """
    Main function to run the game
    """
    player_name = welcome()
    wod = str(wod_pick())
    os.system('clear')
    print(wod)
    print(f"Welcome {player_name}")
    guess_input(wod)


main()