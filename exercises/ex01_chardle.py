"""EXO1 - Chardle - A cute step toward Wordle."""

__author__ = "730245028"

"""Variables:"""
word_guess: str = input("Enter a 5-character word: ")
if len(word_guess) != 5:
    print("Error: Word must contain 5 Characters.")
    exit()

character_guess: str = input("Enter a single character: ")
if len(character_guess) != 1:
    print("Error: Character must be a single character.")
    exit()

count: int = 0

"""Index:"""
print("Searching for " + character_guess + " in " + word_guess)
if character_guess == word_guess[0]:
    print(character_guess + " found at index 0")
    count = count + 1
if character_guess == word_guess[1]:
    print(character_guess + " found at index 1")
    count = count + 1
if character_guess == word_guess[2]:
    print(character_guess + " found at index 2")
    count = count + 1
if character_guess == word_guess[3]:
    print(character_guess + " found at index 3")
    count = count + 1
if character_guess == word_guess[4]:
    print(character_guess + " found at index 4")
    count = count + 1

"""Instances of:"""
if count == 0:
    print("No instances of " + character_guess + " found in " + word_guess)
if count == 1:
    print("1 instance of " + character_guess + " found in " + word_guess)
else:
    print(str(count) + " instances of " + character_guess + " found in " + word_guess)