"""Structured Wordle!"""

__author__ = "730245028"


def contains_char(secret_word: str, chr_guess: str) -> bool:
    """Checks secret word indexes for character guesss."""
    assert len(chr_guess) == 1
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == chr_guess:
            return True
        i = i + 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Codifying green/white/yellow box."""
    assert len(guess_word) == len(secret_word)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    while i < len(guess_word):
        if contains_char(secret_word, guess_word[i]):
            if secret_word[i] == guess_word[i]:
                result = result + GREEN_BOX
            else:
                result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        i = i + 1
    return result


def input_guess(expected_length: int) -> str:
    """Checking for word length."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    guess_length: int = len(guess_word)
    while expected_length != guess_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
        guess_length = len(guess_word)
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    expected_length: int = len(secret_word)
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess_word: str = input_guess(expected_length)
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {turn}/6 turns!")
            return
        turn = turn + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()