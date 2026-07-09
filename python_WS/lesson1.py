import random
play = "yes"
computa = ["rock", "paper", "scissors"]

def processPlayerRock(computer_choice):
    if computer_choice == "scissors":
        print("You won, computa chose scissors")
    elif computer_choice == "paper":
        print("You lost, computer chose paper")
    else:
        print("You drew, computer chose rock")

def processPlayerPaper(computer_choice):
    if computer_choice == "rock":
        print("You won, computa chose rock")
    elif computer_choice == "scissors":
        print("You lost, computer chose scissors")
    else:
        print("You drew, computer chose paper")
        
def processPlayerScissors(computer_choice):
    if computer_choice == "paper":
        print("You won, computa chose paper")
    elif computer_choice == "rock":
        print("You lost, computer chose rock")
    else:
        print("You drew, computer chose scissors")

while play == "yes":
    poopybut = computa[random.randint(0, 2)]
    playerval = input("rock paper or scissors: ")

    if playerval == "rock": # Player choser rock
        processPlayerRock(poopybut)
    elif playerval == "scissors": # Player chose scissors
        processPlayerScissors(poopybut)
    else: # Player chose paper
        processPlayerPaper(poopybut)

    play = input("continue yes or no ")

