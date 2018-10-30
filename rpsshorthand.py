# runs in terminal
# import the randow package so that we can generate random numbers
from random import randint

# life counter for player and computer
playerLives = 3
computerLives = 3

# choices is an array => a container that can hold multiple items
# arrays are 0 based => the first item is 0, the second is 1, etc.
choices = ["Rock", "Paper", "Scissors"]

# game over variables
computerLives <= 0
playerLives <= 0


# visual line break makes text easier to read
line = "\n-------------------------------------\n"
win = "- You win!"
lose = "- You lose!"

# make the computer choose a weapon from the choices array at random
computerChoice = choices[randint(0, 2)]

# print the choice to the terminal window
print(line)
print("Welcome to Kayla's Rock, Paper, Scissors Game!")
# put 'print("Computer chooses:", computerChoice)' here for testing
# (no quotation marks)
print(line)

# set up our loop
while True:

    # check if player lives or computer lives are at 0 first

    # player loses if player lives are 0
    # Exits game (exits loop) or prompt to play again
    if playerLives <= 0:
        print("You lost 3 times! You LOSE! Game Over.\n")
        print("Play Again?")
        player = input("Yes or No?\n").capitalize()
        if player == "Yes":
            playerLives = 3
            computerLives = 3
            print(line)
        elif player == "No":
            print(line)
            print("Thanks for playing!")
            print(line)
            break  # break exits the infinite loop
        else:
            print("\nThat's not a valid choice. Try checking your spelling.\n")
            continue  # puts code back at top of loop

    # player wins if computer lives are 0
    elif computerLives <= 0:
        print("You beat the computer 3 times! You WIN! Game Over.\n")
        print("Play Again?")
        player = input("Yes or No?\n").capitalize()
        if player == "Yes":
            playerLives = 3
            computerLives = 3
            print(line)
        elif player == "No":
            print(line)
            print("Thanks for playing!")
            print(line)
            break
        else:
            print("\nThat's not a valid choice. Try checking your spelling.\n")
            continue

    # ask for player choice after verifying computer and player have 1 life
    print("Your lives:", playerLives)
    print("Computer lives:", computerLives)
    print("\nChoose your weapon!\n")
    player = input("Rock, Paper, or Scissors?\n").capitalize()

    # validates player input
    # if not valid, restarts loop
    if player != choices[0] and player != choices[1] \
       and player != choices[2] and player != "Quit":
        print("\nThat's not a valid choice. Try checking your spelling.\n")
    else:
        # prints selection
        print(line)
        print("You chose", player)
        print("Computer chose", computerChoice)

        # quit section runs before other options
        if player == "Quit":
            print(line)
            print("Goodbye")
            print(line)
            exit()

        # check for a tie = choices are the same
        elif player == computerChoice:
            print("Tie! You live to shoot another day.")

        # check to see if the computer choice beats player choice or not
        # losing
        elif (computerChoice == 0 and player == 2 or (computerChoice > player)):
                print("Computer chose:", computerChoice, "You chose:", player, lose)
                # lose life counter
                playerLives -= 1

        # winning
        elif (player == 0 and computerChoice == 2 or (player > computerChoice)):
                print("Computer chose:", computerChoice, "You chose:", player, win)
                # lose life counter
                computerLives -= 1
        print(line)

    # re-picks computer choice
    # without it, computer picks same weapon each time
    computerChoice = choices[randint(0, 2)]
