# Runs in terminal
# Import the randow package so that we can generate random numbers
from random import randint

# Choices is an array => a container that can hold multiple items
# arrays are 0 based => the first item is 0, the second is 1, etc.
choices = ["Rock", "Paper", "Scissors"]

# Make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

# Print the choice to the terminal window
print("Computer chooses:", computer_choice)

# figure out how to do player choice! BEWARE OF BAD CODE ON THE INTERNET!!!!