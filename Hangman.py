# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def is_valid_input(letter_guessed):
    """
    this function check if the guessed is valid
    :param letter_guessed represent the user input
    :return True if the input is valid otherwise False
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    check if the input is valid and the user didn't us the guessed before
    :param letter_guessed: the user guess
    :param old_letters_guessed: list of all the guessed before
    :return: True if the guess is valid and new
    """
    return is_valid_input(letter_guessed) and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        old_letters_guessed.sort()
        x = "->".join(old_letters_guessed)
        print("X\n", x)
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    ans =[" _"]*len(secret_word)

    for letter in old_letters_guessed:
        if letter in secret_word:
           for i in range(len(secret_word)):
               if letter == secret_word[i] or letter == secret_word[i].upper():
                   ans[i]=" "+letter
               else:
                   if ans[i] != " _":
                       continue
                   else:
                        ans[i]=(" _")
    return "".join(ans)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HANGMAN_ASCII_ART = """Welcome to the game Hangman      _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""

    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART + " \n", MAX_TRIES)
    print(show_hidden_word("shismon",["s","h"]))
    guess = input("Guess a letter:")
    if len(guess) > 1 and guess.isalpha():
        print("E1")
    elif not guess.isalpha() and len(guess) == 1:
        print("E2")
    elif not guess.isalpha() and len(guess) > 1:
        print("E3")
    else:
        print(guess)
        list = ["a", "b"]

    try_update_letter_guessed(guess, list)
    print(list)
    # print(check_valid_input(guess, list))
    # print(is_valid_input(guess))
    guess_word = input("Please enter a word:")
    underscore_number = "_ " * len(guess_word)
    print(underscore_number)
