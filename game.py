
# Get build-in randint function from random module
from random import randint

# Greet player and get player name
player_name = raw_input("Hello - what is your name? ")
print "Hi %s, I'm thinking of a number between 1 and 100." % player_name
# Prompt player to guess a number between 1 and 100
guess = int(raw_input("What is your guess? "))

# Generate a random number between 1 and 100
computer = randint(1, 100)

guessed_it = False
# Create a loop that continues until the user guesses the correct number
while guessed_it == False:
    # Provide feedback if the guess is too high, low, or correct
    if guess > computer:
        guess = int(raw_input("Your guess is too high! Please guess again. "))
    elif guess < computer:
        guess = int(raw_input("Your guess is too low! Please guess again. "))
    else:
        print "Congratulations!  You guessed correctly."
        guessed_it = True

