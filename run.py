# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# testing variable as the word of the day
wod = "plate"

def guess_input():
    print("what is your guess?\n")
    guess = input("your guess:")
    if (guess.lower() == wod):
        print(f"That's correct! {guess.upper()} is the word of the day")
    else:
        print(f"Oops! That guess is wrong. BYE!")

guess_input()