"""One Shot Wordle!"""

__author__ = "730245028"

"""Variables."""
secret: str = "secrets"
wordlength: int = len(secret)
guess: str = input(f"What is your {wordlength}-letter guess? ")
i: int = 0
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
            result = result + WHITE_BOX
        i = i + 1
    
    print(result)

    if secret == guess: 
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")