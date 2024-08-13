# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Library to enable control over clearing the display
import os

# testing variable as the word of the day
wod = "plate"

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


def guess_input():
    """
    Prompts user for guess input
    """
    print("what is your guess?\n")
    guess = input("your guess:")
    if (guess.lower() == wod):
        print(f"That's correct! {guess.upper()} is the word of the day")
    else:
        print(f"Oops! That guess is wrong. BYE!")


def main():
    player_name = welcome()
    os.system('clear')
    print(f"Welcome {player_name}")
    guess_input()


main()