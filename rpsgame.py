# import the random package so that wec an generate random numbers
from random import randint
# choose the rock paper scissors options
# arrays are 0 - based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

playerLives = 3
computerLives = 3

line = "============================================"

# make the computer chose a weapon from the random
computer_choice = choices[randint(0, 2)]
# print the choise to the terminal window
print("Computer chooses: ", computer_choice)
# set up our loop
while player is False:

    # set player to True by making a selection

    print(line)
    print("Player lives:", playerLives, "/5")
    print("Computer lives:", computerLives, "/5")
    print(line)
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")
    print(player, "\n")

    if player == computer_choice:
        print("Tie! You live to shoot another day")

    elif player == "Rock":
        if computer_choice == "Paper":
            print("You Lose! Paper covers Rock")
            playerLives = playerLives - 1
        else:
            print("Yon Win!", player, "smashes", computer_choice)
            computerLives = computerLives - 1

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You Lose!", computer_choice, "cut", player)
            playerLives = playerLives - 1
        else:
            print("You won!", player, "covers", computer_choice)
            computerLives = computerLives - 1

    elif player == "Scissors":
        if computer_choice == "Rock":
            print ("You lose!", computer_choice, "smashes", player)
            playerLives = playerLives - 1
        else:
            print("You Win!", player, "cut", computer_choice)
            computerLives = computerLives - 1

    elif player == "quit":
        exit()

    else:
        print("Check your spelling...that's not a valid choice\n")

if playerLives is 0:
    print("You're out of lives! Would you like to play again?")

    choice = input("Y / N ?").captialize()

    if choice == "Y":
        playerLives = 5
        computerLives = 5
        player = False
        computer_choice = choices[randint(0, 2)]
    elif choice == "N":
        print("You've had enough losing")
        exit()

if computerLives is 0:
    print("You're out of lives! Would you like to play again?")

    choice = input("Y / N ?").captialize()

    if choice == "Y":
        playerLives = 5
        computerLives = 5
        player = False
        computer_choice = choices[randint(0, 2)]
    elif choice == "N":
        print("You've had enough losing")
        exit()
