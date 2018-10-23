# runs in terminal
# import the randow package so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0 based => the first item is 0, the second is 1, etc.
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

# print the choice to the terminal window
print("Computer chooses:", computer_choice)

# set up our loop
while player is False:
	#set player to True by making a selection
	print("Choose your weapon! (Case sensitive)")
	print("Or Quit")
	player = input("Rock, Paper, or Scissors?\n")

	print(player, "\n")

	# check for a tie = choices are the same
	if player == computer_choice:
		print("Tie! You live to shoot another day.")

	# check to see if the computer choice beats player choice or not
	elif player == "Rock":
		if computer_choice == "Paper":
			# computer wins *sad face*
			print("Paper covers Rock. You lose! Try again")
		else:
			# we win! such winning
			print(player, "smashes", computer_choice, "You win!")

	elif player == "Paper":
		if computer_choice == "Scissors":
			print(computer_choice, "cut", player, "You lose!")
		else:
			print(player, "covers", computer_choice, "You win!")

	elif player == "Scissors":
		if computer_choice == "Rock":
			print(computer_choice, "smashes", player, "You lose!")
		else:
			print(player, "cut", computer_choice, "You win!")

	elif player == "Quit":
		exit ()
	else:
		print("That's not a valid choice... try checking your spelling\n")

	player = False
	computer_choice = choices[randint(0, 2)] 

# add player lives and computer lives somewhere (incrementing or decrementing lives + outputting message for those conditions)
# type in win or lose variables for winning and losing 
# have to type script to display the number of lives
# final script to let the player quit or play again

