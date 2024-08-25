import os
import random
import math
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# based on love sandwiches project to get access to a
# google sheets document and record scores and call
# the highest for comparison
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Wordle-game')

# Sets constant to use to call on scores worksheet
SCORES = SHEET.worksheet('scores')

# Specifies character display size to map prints
DISPLAY = {"x": 80, "y": 24}


class Style:
    """
    text formatting and colours based on stackoverflow article
    https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    using ANSI codes found on wikipedia
    https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit
    """
    BLAKCFG = '\033[30m'
    BLACKBG = '\033[40m'
    REDBG = '\033[41m'
    GREENBG = '\033[42m'
    YELLOWBG = '\033[43m'
    BLUEBG = '\033[44m'
    PURPLEBG = '\033[45m'
    CYANBG = '\033[46m'
    WHITEBG = '\033[47m'
    GREYBG = '\033[100m'
    BGTREDBG = '\033[101m'
    BGTGREENBG = '\033[102m'
    BGTYELLOWBG = '\033[103m'
    BGTBLUEBG = '\033[104m'
    BGTPURPLEBG = '\033[105m'
    BGTCYANBG = '\033[106m'
    BGTWHITEBG = '\033[107m'
    BOLD = '\033[1m'
    INVERT = '\033[7m'
    PLAIN = '\033[0m'

style_test = ""
style_test += f"{Style.BOLD}{Style.GREENBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.BLACKBG} B {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.BGTYELLOWBG}{Style.BLAKCFG} A {Style.PLAIN}\n\n"
style_test += f"{Style.BOLD}{Style.REDBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.YELLOWBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.PURPLEBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.CYANBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.WHITEBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.GREYBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTREDBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTGREENBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTYELLOWBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTBLUEBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTPURPLEBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTCYANBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"
style_test += f"{Style.BOLD}{Style.BGTWHITEBG} A {Style.PLAIN}"
style_test += f"{Style.BOLD}{Style.GREYBG} B {Style.PLAIN}\n"

print(style_test)
input('ready?')


class User:
    """ Class to define information stored for player. """
    def __init__(self, name):
        """
        Initializes user object with name only
        and creates attributes to collect data
        from the game.

        Args:
          name: string: The name the player gives
            themselves at the start of the game.
        """
        self.id = int(timestamp())
        self.name = name
        self.streak = 0
        self.highscore = 0
        self.guesses = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
        self.add_session()

    def result(self):
        """
        The output at the end of the game to display
        the player's scores and compiled messages.

        Returns:
          string: Compiled string from user data
            collected in the game.
        """
        message = ""

        if self.streak == 0:
            message += f"Oh no, {self.name}! You've lost this streak!\n"
        else:
            message += f"Nicely done, {self.name}!\n"

        message += f"Your current streak: {self.streak}. "
        message += f"and longest streak: {self.highscore}\n"
        message += f"On average, you have guessed the word of the day in {self.guess_average()} guesses.\n"
        self.update_session()
        message += f"You have ranked {self.rank()}\n"

        return message

    def add_session(self):
        """ Adds User data to database to record session start """
        line = [self.id, self.name, self.streak, self.highscore]

        # compiles integers from guesses as list
        record = []
        record.extend(self.guesses.values())

        # adds record to list of values to add to worksheet
        line.extend(record)

        # sets initial value of average_guess to zero
        average_guess = 0
        line.append(average_guess)

        # adds game session to worksheet
        SCORES.append_row(line)


    def update_session(self):
        """
        Lookup the session timestamp/ID of the 
        current player and update the row in the
        worksheet with the lastest data.
        """
        # find the cell with the current player id
        cell = SCORES.find(str(self.id))

        # compile a list of user data again
        line = [self.id, self.name, self.streak, self.highscore]

        # compile a list of integers of games won with a given number of turns taken
        record = []
        record.extend(self.guesses.values())
        line.extend(record)

        # call function to calculate guess average to add to list of values
        average_guess = self.guess_average()
        line.append(average_guess)

        # update row of the matching ID with compiled list
        SCORES.update([line],cell.address)


    def guess_average(self):
        """
        Calculate the average number of turns 
        the current player has taken to guess
        the word of the day correctly.

        Returns: float: calculated average number
          of guesses over the times the player has
          managed to guess the word.
        """
        # compile a list of integers of games won with
        # a given number of turns taken.
        record = []
        record.extend(self.guesses.values())

        average_guess = 0

        # list comprehension which converts the list
        # of games won by number of guesses to a total
        # number of guesses made resulting in a win.
        total_guesses = [record[x] * (x + 1) for x in range(6)]

        # if player has guessed any of the words so far
        # divide the total number of guesses by the number
        # of won games and round the number to 2 decimal points.
        if math.fsum(record) != 0:
            average_guess = math.fsum(total_guesses)/math.fsum(record)
            average_guess = round(average_guess, 2)
        else:
            pass

        return average_guess


    def rank(self):
        """
        Compares the player's highscore to those on the worksheet.
        Lookup the longest_streak column and find the index of
        the player's highscore.

        Returns: string: compiled of index the player has been
          found and how many games have been played.

        """
        # fetch worksheet values of highscores
        highscore_list = SCORES.col_values(4)

        # sort in descending order
        highscore_list.sort(reverse=True)

        # finds the index of the player in the list
        place = highscore_list.index(str(self.highscore))

        # counts the number of game entries, minus heading
        total = len(highscore_list) - 1

        # compiles string with data above
        message = f" {place} of {total}!"
        return message


def timestamp():
    """
    Creates a string of numbers alone from date and time
    
    Returns: string: of number characters only in the format
    of year as 2 digits, week number, hours, minutes and seconds.
    """
    x = datetime.now()
    stamp = f'{x.strftime("%y")}{x.strftime("%W")}{x.strftime("%X")}{str(x.strftime("%f"))[0]}{str(x.strftime("%f"))[1]}'
    return stamp.replace(":","")


def welcome():
    """
    Produces the welcome screen into the game including
    the player name input.

    Returns:
      string: player name to create user object.
    """
    # Welcome message broken up into the segments to printout in lines
    wlc_msg = ['Welcome', '', 'to', '', 'Wordle']

    # Calculate the starting line for the welcome message
    # accounts for the number of lines the message requires
    # substracts from the display height and divides it in half
    msg_start_ln = int((DISPLAY['y'] - len(wlc_msg))/2)

    # prints the number of blank lines to reach the
    # line the message starts at
    for line in range(msg_start_ln):
        print()

    # prints each value of the message list in a new line
    # with center alignment
    for line in wlc_msg:
        print(f"{line.center(DISPLAY['x'])}")

    # prints the number of blank lines until 2 lines short so
    # prompt appears for the player to introduce themselves
    for line in range(DISPLAY['y']-(msg_start_ln + len(wlc_msg) + 2)):
        print()

    # prompt for player to enter name and removes whitespaces
    # before or after input string
    plr_name = input("What's your name?\n").strip()

    # sets default player name should input be blank
    if plr_name == "":
        plr_name = "Player-1"

    return plr_name


def help():
    """
    A function to display instructions for the game
    whenever the user enters 'help!' as a guess.
    """
    # Clear previous guess messages
    os.system('clear')

    print("help is at hand!")
    input("Ready to resume the game? press ENTER")


def display_guesses(data, wod):
    """
    Generate the UI by displaying guesses and providing
    clues as to which letters have been guessed correctly,
    via colour coding of each character.

    Args:
      data: list of str: the list of guesses the player
        has made so far.
      wod: string: Word Of (the) Day the word randomly
        selected for this game to compare the guesses
        against.
    """
    # generates a dictionary to lookup number of occurences of
    # each letter in the word of the day
    wod_dict = {x: wod.count(x) for x in wod}

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
            # for each character, check which letters and places were guessed
            # correctly
            for place in range(5):
                if word[place] == wod[place]:
                    accuracy.append("C")
                    tally[word[place]] -= 1
                else:
                    accuracy.append("X")
            # second pass, checks if letter but NOT places were guessed
            # correctly
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


def validate_input(value):
    """
    Validates input against our criteria:
    - 5 characters long
    - all characters are letters
    - input is a word in our dictionary

    Args:
      value: string: the lastest entry by the player for
        a guess, before it is added to the guesses list

    Returns:
      boolean: True or False, of whether the entry is
        valid or not.
    """
    try:
        # User asks for help to review the rules
        if value == "help!":
            help()

        # Start - very similar to the love sandwiches validate data
        elif len(value) != 5:
            raise ValueError(
                f"The game only accepts 5 letter inputs, you provided "
                + f"{len(value)}"
            )
        # End - very similar to the love sandwiches validate data

        # Check the string is all alphabetic characters only
        elif not value.isalpha():
            raise ValueError(
                f"This is a word game, you guess includes characters not "
                + "in the alphabet"
            )

        # Check the word in the string is a word in our dictionary
        elif not dict_check(value):
            raise ValueError(
                f"Your guess, {value.upper()} is not a word in our dictionary"
            )

    # Start - very similar to the love sandwiches validate data
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return False

    return True
    # End - very similar to the love sandwiches validate data


def guess_input(word, player):
    """
    Displays a welcome message to the playes and prompts
    player for guess input.

    Args:
      word: string: the randomly selected word for the
        game to compare all guesses against.
      player: list of User: the user attributes and
        methods we call and feed to in the game.
    """
    print(f"Welcome {player.name}. To reveal rules, type 'help!'.")

    print('\n')

    # list to hold player guesses
    guesses = []

    # display blank lines
    display_guesses(guesses, word)

    # loops below until either the correct guess is made
    while True:
        print("what is your guess?\n")
        guess = input("your guess:").strip()

        # Clear previous guess messages
        os.system('clear')

        print(f"Welcome {player.name}. To reveal rules, type 'help!'.")
        print('\n')

        # trigger function to display the guesses made to the CLI,
        # even when an invalid guess has been made
        display_guesses(guesses, word)

        # validates input
        if validate_input(guess.lower()):
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

            # if guess is correct, print message confirming so and breaks
            # the loop
            if (guess.lower() == word):
                player.guesses[str(len(guesses))] += 1
                player.streak += 1
                player.highscore = max(player.streak, player.highscore)
                print(f"That's correct! {guess.upper()} is the word of"
                      + " the day.\n")
                print(player.result())
                break

            # or else print message for the player to try again
            else:
                # Whilst player has not made 6 valid guesses, the game goes on
                if len(guesses) < 6:
                    print(f"Oops! That guess is wrong. You have "
                          + f"{6 - len(guesses)} guess(es) left.")
                # After the 6th valid guess the game is over.
                else:
                    player.streak = 0
                    print(f"GAME OVER\nThe selected word was {word.upper()}.")
                    print(player.result())
                    break


def get_dictionary():
    """
    Create list of words from word database.

    Returns: list of strings: words to use as a dictionary.
    """
    f = open('en-us-dict.txt')

    # creates the list of strings a global variable
    global words
    words = [word for word in f.readlines() if word.strip()]
    f.close()


def dict_check(value):
    """
    Checks if value given is in the dictionary,
    returns True or False.

    Args:
      value: string: The player's latest guess.

    Returns:
      boolean: True or False, if the word is in
        the word bank text file
    """
    return value in words or f"{value}\n" in words


def main():
    """ Main function to run the game. """
    player = User(welcome())

    get_dictionary()

    while True:
        # Word Of the Day being randomly selected
        wod = random.choice(words).strip()

        os.system('clear')
        guess_input(wod, player)

        # After playing the game, ask for input to confirm new game
        new_round = input('Enter "n" to quit or any key to play again: ')

        if new_round.lower().strip() == 'n':
            print(f'Thank you for playing, {player.name}. Goodbye.')
            return False


main()
