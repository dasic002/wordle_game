# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Library to enable control over clearing the display
import os

# Library for pseudo random functions
import random

# Specifies character display size to map prints
DISPLAY = {"x": 80, "y": 24}

wlc_msg = ['Welcome', '', 'to', '', 'Wordle']


def welcome():
    """
    Produces the welcome screen into the game including the player name input
    """
    msg_start_ln = int((DISPLAY['y'] - len(wlc_msg))/2)

    for line in range(msg_start_ln):
        print()

    for ln in wlc_msg:
        print(ln.center(DISPLAY['x']))
    
    for line in range(DISPLAY['y']-(msg_start_ln + len(wlc_msg) + 2)):
        print()

    plr_name = input("What's your name?\n")
    return plr_name


def wod_pick():
    """
    Random selecting a 5 letter word from the word bank file
    """
    f = open('en-us-dict.txt')
    words = f.readlines()
    f.close()
    return random.choice(words).strip()


def dict_check(value):
    """
    Checks if value given is in the dictionary
    returns True or False
    """
    f = open('en-us-dict.txt')
    words = f.readlines()
    f.close()
    return value in words or f"{value}\n" in words


def guess_input(word):
    """
    Prompts user for guess input
    """
    print(word)
    while True:
        print("what is your guess?\n")
        guess = input("your guess:")

        if validate_input(guess.lower()) == True:
            print("data is valid!")
            break
    
    if (guess.lower() == word):
        print(f"That's correct! {guess.upper()} is the word of the day")
    else:
        print(f"Oops! That guess is wrong. BYE!")


def validate_input(value):
    """
    Validates input against our criteria:
    - 5 characters long
    - all characters are letter
    - input is a word in our dictionary
    """
    try:
        # Start - very similar to the love sandwiches validate data
        if len(value) != 5:
            raise ValueError(
                f"The game only accepts 5 letter inputs, you provided {len(value)}"
            )
        # End - very similar to the love sandwiches validate data

        # Check the string is all alphabetic characters only
        elif value.isalpha() == False:
            raise ValueError(
                f"This is a word game, you guess includes characters not in the alphabet"
            )
        
        # Check the word in the string is a word in our dictionary
        elif dict_check(value) == False:
            raise ValueError(
                f"Your guess, {value.upper()} is not a word in our dictionary"
            )

    # Start - very similar to the love sandwiches validate data
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return False

    return True
    # End - very similar to the love sandwiches validate data


def main():
    """
    Main function to run the game
    """
    player_name = welcome()
    wod = str(wod_pick())
    os.system('clear')
    print(f"Welcome {player_name}")
    guess_input(wod)


main()