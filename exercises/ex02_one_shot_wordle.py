"""EX02 - One Shot Wordle - Basically Almost Wordle"""

__author__ = "730470086"


secret: str = "python"
word: str = input(f"What is your {len(secret)}-letter guess? ")
counter: int = 0
emoji: str = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


while len(secret) != len(word):
    word: str = input(f"That was not {len(secret)} letters! Try again: ")

while len(secret) == len(word):
    if secret == word:
        print("Woo! You got it!")
        quit()
        while counter < len(secret):
            if word[counter] == secret[counter]:
                emoji += green_box
            else: 
                emoji += white_box
    else:
        print("Not quite. Play again soon!")
        quit()







