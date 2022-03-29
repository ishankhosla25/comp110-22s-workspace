"""One Shot Wordle!"""

__author__ = "730245028"

"""Variables."""
secret: str = "slimey"
wordlength: int = len(secret)
guess: str = input(f"What is your {wordlength}-letter guess? ")
i: int = 0
otherspot: bool = False
true: bool = True
otherindex: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = ""

while len(secret) != len(guess):
    print(f"That was not {wordlength} letters! Try again: { guess }")
    guess: str = input(f"What is your {wordlength}-letter guess? ")

if len(secret) == len(guess):
    while i < wordlength:
        if guess[i] == secret[i]:
            result = result + GREEN_BOX
        else:
            while otherspot != true and otherindex < wordlength:
                if guess[i] == secret[otherindex]:
                    otherspot = not(otherspot)
                    result = result + YELLOW_BOX
                otherindex = otherindex + 1
            if otherspot != true:
                result = result + WHITE_BOX
        otherindex = 0
        otherspot = False            
        i = i + 1

print(result)

if secret == guess: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")