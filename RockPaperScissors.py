from random import *
from time import *
RockPaperScissors = ["ROCK", "PAPER", "SCISSORS"]
PlayerChoices = ["ROCK", "PAPER", "SCISSORS", "GUN"]
BotAns = choice(RockPaperScissors)
print("Rock!")
sleep(0.5)
print("Paper!")
sleep(0.5)
print("Scissors!")
sleep(0.5)
print("Shoot!")
choice = str.upper(input())
IsAChoice = False
while not IsAChoice:

    if choice in PlayerChoices:
        IsAChoice = True
        pass
    else:
        choice = str.upper(input("Rock, paper, or scissors! Not anything else!"))
if choice == "ROCK":
    if BotAns == "PAPER":
        print("I got paper! I win hahahaha")
        exit()
    elif BotAns == "SCISSORS":
        print("You got me! I promise to get you next time!")
        exit()
    else:
        print("well, well, well, seems as though we have tied. I will beat you next time! I swear MY LIFE ON IT!")
        exit()
elif choice == "PAPER":
    if BotAns == "SCISSORS":
        print("I got Scissors! I win hahahaha")
        exit()
    elif BotAns == "ROCK":
        print("You got me! I promise to get you next time!")
        exit()
    else:
        print("well, well, well, seems as though we have tied. I will beat you next time! I swear MY LIFE ON IT!")
        exit()
else:
    if BotAns == "ROCK":
        print("I got ROCK! I win hahahaha")
        exit()
    elif BotAns == "PAPER":
        print("You got me! I promise to get you next time!")
        exit()
    else:
        print("well, well, well, seems as though we have tied. I will beat you next time! I swear MY LIFE ON IT!")
        exit()
