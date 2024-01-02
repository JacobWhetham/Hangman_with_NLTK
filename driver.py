"""
    :author:        Jacob Whetham
    :version:       1.0.0, 02 JAN 2024
    :desc:          This program creates the classic hangman game for the user to play.
"""

# Imports
import hangman  # Allows for use of the Hangman game.


# Runs the program.
def startProgram():
    # While True (an infinite loop),
    while True:
        hangman_instance = hangman.hangman() # Creates an instance of the Hangman game.

        # The below code only executes once the Hangman game is completed.

        play_again = input("Enter 'y' to play again, or anything else to exit. ").lower() # Captures the user's desire to play again.

        # If the user responded with 'y',
        if (play_again == 'y'):
            hangman_instance = None # Resets the Hangman instance.
            continue # Restarts the loop.

        # Otherwise (the user does not want to play again),
        else:
            break # Exits the infinite loop.

    # The below code only executes once the infinite loop is broken.

    print("Goodbye!") # Outputs a goodbye message.
    exit(0) # Exits the program.


# Runs once the program starts.
if __name__ == "__main__":
    startProgram() # Runs the program.