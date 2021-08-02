# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.






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
    print(HANGMAN_ASCII_ART+" \n",MAX_TRIES)

    guess = input("Guess a letter:")
    print(guess)
