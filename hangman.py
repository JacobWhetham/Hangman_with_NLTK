"""
    :author:        Jacob Whetham
    :version:       1.0.0, 02 JAN 2024
    :desc:          This file contains the functionality of the Hangman game by utilizing NLTK to generate words.
"""

# Imports
import nltk # Allows use of the Natural Language Toolkit

nltk.download('wordnet')                    # Downloads WordNet data for working with the words.

from nltk.corpus import wordnet      # Allows use of Words and WordNet functionality.
from random import sample                   # Allows use of taking a random sample from an iterable.

# This class allows creation of an instance of the Hangman game.
class hangman:
    # Declare global variables
    word = []                       # Holds the randomly selected word.
    guesses = []                    # Holds the user's guesses.
    lives = 6                       # Holds the user's remaining lives.
    game_should_run = True          # Holds whether the game should end.

    # The default constructor.
    def __init__(self):
        # Ensures all the values of the instance are the default.
        self.word = []
        self.guesses = []
        self.lives = 6
        self.game_should_run = True

        self.createGame()   # Creates the game.


    # Creates the Hangman game.
    def createGame(self):
        difficulty = self.determineDifficulty() # Gathers the difficulty setting from user input.

        # Gathers only words applicable to the difficulty rating based on string length.
        list_of_words = [word for word in wordnet.words() if len(word) >= difficulty * 2 and len(word) <= difficulty * 4 and not word[0].isupper() and not "_" in word]
        self.word = sample(list_of_words, 1) # Sets the word to be a single random sample from the applicable words.

        self.updateGameDisplay() # Updates the game's display by drawing the hangman's stand.

        # While the game is running,
        while self.game_should_run == True:
            self.gameLoop() # Processes the game's loop (updating the display, asking for input) every iteration.

        # The below code is only reached when the game is no longer running.

        self.finishGame() # Finishes the game.


    # Ends the game.
    def finishGame(self):
        syns = wordnet.synsets(self.word[0]) # Determines the synonym sets for the word.
        definition = syns[0].definition() # Captures the definition of the word.
        print(f"The word was {self.word[0]}. It means: {definition}") # Outputs the word and its definition.


    def determineDifficulty(self) -> int:
        """
                    Determines the difficulty of the game.
        :return:    The integer corresponding with the difficulty level (larger = more difficult).
        """

        # While True (an infinite loop),
        while True:

            # Attempts to,
            try:
                # Captures the user's input as an integer for the difficulty.
                difficulty = int(input("What difficulty would you like?" + "\n" +
                                       "1 - Easy" + "\n" +
                                       "2 - Medium" + "\n" +
                                       "3 - Hard" + "\n" +
                                       "4 - Absurd" + "\n"))

            # Except if an integer cannot be gathered,
            except Exception:
                print("Please enter an integer!") # Outputs an error.
                continue # Restarts the loop.

            # The below code only executes if the Try-block was successful.

            # If the difficulty is less than 1 or greater than 4,
            if difficulty < 1 or difficulty > 4:
                print("Please enter an integer only between 1 and 4.") # Outputs an error.
                continue # Restarts the loop.

            # The below code only executes if the difficulty is valid (between 1 and 4, inclusive).

            return difficulty # Returns the difficulty level.


    # Handles the game's loop.
    def gameLoop(self):
        print(f"Your current guesses: {self.guesses}")  # Outputs the user's current guesses.
        guess = input("What's your guess? ").lower()    # Asks for the user's next guess.

        # If the user's guess is not a letter,
        if not guess.isalpha():
            print("You must guess a letter!")   # Outputs an error.
            return  # Leaves the function (will go to the next loop).

        # Otherwise if the length of the user's guess is not 1 (more than one letter was guessed),
        elif len(guess) != 1:
            print("You must guess only one letter!") # Outputs an error.
            return # Leaves the function (will go to the next loop).

        # Otherwise if the user's guess was already used,
        elif guess in self.guesses:
            print("You've already guessed that!") # Outputs an error.
            return # Leaves the function (will go to the next loop).

        # Otherwise (the guess must be valid),
        else:
            self.guesses.append(guess) # Appends the guess to the user's current guesses.
            self.checkGuess(guess) # Checks if the user's guess is in the word.


    def checkGuess(self, guess: chr):
        """
                            Checks if the user's guess is within the word.
        :param guess:       The user's guess.
        """

        # If the guess is in the word,
        if guess in self.word[0]:
            print(f"Good job! '{guess}' is in the word!") # Outputs a success message.

        # Otherwise (the guess is not in the word),
        else:
            self.lives = self.lives - 1 # Decrements the user's remaining lives.

            print(f"Whoops! '{guess}' is not in the word!") # Outputs a failure message.

            # If the user's lives is 0 or less,
            if (self.lives <= 0):
                print(f"You've run out of guesses. Game over!") # Outputs a game over message.
                self.game_should_run = False # Declares that the game should be over.
                self.updateGameDisplay() # Updates the game's display to show the final Hangman diagram.
                return # Leaves the function (will finish up the game).

        # The below code only executes if the user has life remaining (on success or failure).

        self.updateGameDisplay() # Updates the game's display.


    # Updates the game's display.
    def updateGameDisplay(self):
        output = "The word to guess: "  # Stores the output to be printed.

        # Prints the boilerplate of the Hangman's stage.
        print("  ----  ")
        print("  |   |  ")

        # The below code prints the remainder of the Hangman's stage depending on how many lives the user has left.
        if (self.lives == 6):
            print("      |  ")

        elif (self.lives <= 5):
            print("  O   |  ")

        if (self.lives == 4):
            print("  |  ")

        elif (self.lives == 3):
            print(" -|  ")

        elif (self.lives <= 2):
            print(" -|-  ")

        if (self.lives == 1):
            print(" /  ")

        elif (self.lives <= 0):
            print(" / \\  ")
            return  # Leaves the function (the game is over).

        # The below code only executes if the user has remaining lives.

        # For every letter in the word,
        for char in self.word[0]:
            # If the letter is not in the user's current guesses,
            if char not in self.guesses:
                output = output + "_" # Appends an underscore to the output message (the letter is unknown).

            # Otherwise (the letter was already guessed by the user),
            else:
                output = output + char # Appends the letter to the output message.

        # If the output message does not have an underscore (the word was guessed completely),
        if '_' not in output:
            print(f"Congrats! You've guessed the word!") # Outputs a success message.
            self.game_should_run = False # Declares that the game should close.
            return # Leaves the function (the game should end).

        # The below code only executes if there are still unknown letters in the word (the game is not over).

        print(output + "\n") # Outputs the current word with the remaining unknown letters.