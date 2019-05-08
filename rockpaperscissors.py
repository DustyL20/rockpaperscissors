#rock paper scissors
from random import randint

t = ["Rock", "Paper", "Scissors"]

cpu = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, paper, or scissors?")
    if player == cpu:
        print("Tie!")
    elif player == "Rock":
        if cpu == "Paper":
            print("You lose!", cpu, "beats", player)
        else:
            print("You win!", player, "smashes", cpu)
    elif player == "Paper":
        if cpu == "Scissors":
            print("You lose!", cpu, "cut", player)
        else:
            print("You win!", player, "covers", cpu)
    elif player == "Scissors":
        if cpu == "Rock":
            print("You lose...", cpu, "smashes", player)
        else:
            print("You win!", player, "cut", cpu)
    else:
        print("That's not a valid play. Check your spelling!")
            # player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0, 2)]




