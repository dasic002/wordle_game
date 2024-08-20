# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Library to enable control over clearing the display
import os

# Library for pseudo random functions
import random

# Specifies character display size to map prints
DISPLAY = {"x": 80, "y": 24}

# Welcome message broken up into the segments to printout in lines
WLC_MSG = ['Welcome', '', 'to', '', 'Wordle']

# text formatting and colours
# based on stackoverflow article
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
# using ANSI codes found on wikipedia
class Style:
    GREYBG = '\033[100m'
    GREENBG = '\033[42m'
    PURPLEBG = '\033[45m'
    BOLD = '\033[1m'
    PLAIN  = '\033[0m'


class User:
    """
    Class to define information stored for player
    """
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.highscore = 0
        self.guesses = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
    
    def result(self):
        """
        The output at the end of the game to display the player's scores
        """
        message = ""

        if self.streak == 0:
            message += "Oh no! You've lost this streak!\n"
        else:
            message += "Nicely done!\n"

        message += f"Your current streak: {self.streak}\n"
        message += f"Your longest streak: {self.highscore}\n"
        message += f"Number of guesses taken:\n"
        message += f"{self.guesses}"

        return message


def welcome():
    """
    Produces the welcome screen into the game including the player name input
    """
    # Calculate the starting line for the welcome message
    # accounts for the number of lines the message requires
    # substracts from the display height and divides it in half
    msg_start_ln = int((DISPLAY['y'] - len(WLC_MSG))/2)

    # prints the number of blank lines to reach the 
    # line the message starts at
    for line in range(msg_start_ln):
        print()

    # prints each value of the message list in a new line 
    # with center alignment
    for line in WLC_MSG:
        print(f"{line.center(DISPLAY['x'])}")
    
    # prints the number of blank lines until 2 lines short so 
    # prompt appears for the player to introduce themselves
    for line in range(DISPLAY['y']-(msg_start_ln + len(WLC_MSG) + 2)):
        print()

    # prompt for player to enter name
    plr_name = input("What's your name?\n")
    return plr_name


def help():
    """
    A function to display instructions for the game whenever the user
    enters 'help!' as a guess
    """
    # Clear previous guess messages
    os.system('clear')

    print("help is at hand!")
    input("Ready to resume the game? press ENTER")


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


def display_guesses(data, wod):
    """
    Generate the UI by displaying guesses and providing 
    clues as to which letters have been guessed correctly
    """
    # generates a dictionary to lookup number of occurences of 
    # each letter in the word of the day
    wod_dict = {x:wod.count(x) for x in wod}
    
    # produces a list of characters for each guess to help 
    # player deduce the word of the day, will produce 6 lines
    # including blank ones for guesses not made yet
    for num in range(6):
        
        # variable to hold list of letter guessed
        accuracy = []
        # variable to copy wod_dict
        tally = wod_dict.copy()

        # For the words not present while guesses list is not 6 values long 
        # use a wildcard value
        if data == [] or len(data)-1 < num:
            word = "     "
            accuracy = ['X', 'X', 'X', 'X', 'X']

        else:
            word = data[num]
            # for each character, check which letters and places were guessed correctly
            for place in range(5):
                if word[place] == wod[place]:
                    accuracy.append("C")
                    tally[word[place]] -= 1
                else:
                    accuracy.append("X")
            # second pass, checks if letter but NOT places were guessed correctly 
            for idx in range(5):
                if accuracy[idx] == "X" and word[idx] in tally:
                    if tally[word[idx]] > 0:
                        accuracy[idx] = "O"
                        tally[word[idx]] -= 1
                else:
                    pass
                    
        clue_ln = ""
        
        # for each character in the guess add styles for clues
        for x in range(5):
            # all are made bold
            clue_ln += Style.BOLD
            # if correct letter and place, background is green
            if accuracy[x] == "C":
                clue_ln += Style.GREENBG
            # if correct letter but not place, background is purple
            elif accuracy[x] == "O":
                clue_ln += Style.PURPLEBG
            # else it is a grey background
            else:
                clue_ln += Style.GREYBG
            
            clue_ln += f" {word[x].upper()} "
            clue_ln += Style.PLAIN
            clue_ln += " "
        
        print(f"{clue_ln}\n")


def guess_input(word, player):
    """
    Prompts user for guess input
    """
    print(f"Welcome {player.name}. To reveal rules, type 'help!'.")

    # printing the WOD for testing purposes
    print(word)
    print('\n')
        
    # list to hold player guesses
    guesses = []

    # display blank lines
    display_guesses(guesses, word)

    # loops below until either the correct guess is made
    while True:
        print("what is your guess?\n")
        guess = input("your guess:")
            
        # Clear previous guess messages
        os.system('clear')

        print(f"Welcome {player.name}. To reveal rules, type 'help!'.")
        print('\n')
        
        # trigger function to display the guesses made to the CLI, 
        # even when an invalid guess has been made
        display_guesses(guesses, word)

        # validates input
        if validate_input(guess.lower()) == True:
            # confirms guess is valid
            print("data is valid!")

            # add valid guess to list of guesses made
            # since 'help!' bypasses validation, here we 
            # ignore it for appending to guesses. 
            # This allows the rest of the code to refresh 
            # the display and return to the game.
            if guess.lower() != "help!":
                guesses.append(guess)
            
            # Clear previous guess messages so we have no duplicates from above
            os.system('clear')
            
            print(f"Welcome {player.name}. To reveal rules, type 'help!'.")
            print('\n')

            # trigger function to display the guesses made to the CLI
            display_guesses(guesses, word)
            
            # if guess is correct, print message confirming so and breaks the loop
            if (guess.lower() == word):
                player.guesses[str(len(guesses))] += 1
                player.streak += 1
                player.highscore = max(player.streak, player.highscore)
                print(f"That's correct! {guess.upper()} is the word of the day")
                print(player.result())
                break
            
            # or else print message for the player to try again
            else:
                # Whilst player has not made 6 valid guesses, the game goes on
                if len(guesses) < 6:
                    print(f"Oops! That guess is wrong. You have {6 - len(guesses)} guess(es) left.")
                # After the 6th valid guess the game is over.
                else:
                    player.streak = 0
                    print(f"GAME OVER\nThe selected word was {word.upper()}.")
                    print(player.result())
                    break


def validate_input(value):
    """
    Validates input against our criteria:
    - 5 characters long
    - all characters are letter
    - input is a word in our dictionary
    """
    try:
        # User asks for help to review the rules
        if value == "help!":
            help()

        # Start - very similar to the love sandwiches validate data
        elif len(value) != 5:
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
    player = User(welcome())
    wod = str(wod_pick())
    os.system('clear')
    guess_input(wod, player)


main()