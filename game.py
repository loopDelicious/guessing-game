
# Get build-in randint function from random module
from random import randint

# Greet player and get player name
player_name = raw_input("Hello - what is your name? ")
print "Hi {}, I'm thinking of a number between 1 and 100.".format(player_name)

guessed_it = False

# Create a loop that continues until the user guesses the correct number
while guessed_it == False:
    # Generate a random number between 1 and 100
    computer = randint(1, 100)
    attempts = 0
    
    while guessed_it == False:

        try:   # Error message if user does not guess a number
            guess = int(raw_input("What's your guess? "))
        except ValueError:
            print "That's not a valid number, try again."
            continue

        if guess > 100 or guess < 1:  # Error message if user guesses out of range
            print "Out of range. Please guess again."
            continue

        # Add an attempt on this round
        attempts += 1
        # Provide feedback if the guess is too high, low, or correct
        if guess > computer:
            print "Your guess is too high! Please guess again. "
        elif guess < computer:
            print "Your guess is too low! Please guess again. "
        else:
            print "Congratulations!  You guessed correctly."
            print "It took you {} tries!".format(attempts)
            guessed_it = True


    play_again = raw_input("Would you like to play again - Y or N? ")
    if play_again != "Y":
        break

    