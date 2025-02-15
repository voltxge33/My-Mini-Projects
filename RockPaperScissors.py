from random import *
from time import *
print("Welcome to rock paper scissors! Made by: Oliver\nQuotes from: Oliver, Quinlan, and Ms.Mosher")
RPSYES = ["Y","YES","SURE","OKAY", ""]
RPSchoice = input("Would you like to play? (Y/N): ")
def RPS():
    RockPaperScissors = ["ROCK", "PAPER", "SCISSORS"]
    PlayerChoices = ["ROCK", "PAPER", "SCISSORS", "GUN", "MRFORBIS", "MR FORBIS", "TRUMP", "ELON", "BOOK", "TRUMPANDELONFOREVA"]
    BotAns = choice(RockPaperScissors)
    print("Rock!")
    sleep(0.5)
    print("Paper!")
    sleep(0.5)
    print("Scissors!")
    sleep(0.5)
    print("Shoot!")
    sleep(0.5)
    pchoice = str.upper(input("What's your play?: "))
    IsAChoice = False
    while not IsAChoice:

        if pchoice in PlayerChoices:
            IsAChoice = True
            pass
        else:
             pchoice = str.upper(input("Rock, paper, or scissors! Not anything else: "))
        if pchoice == "ROCK":
            if BotAns == "PAPER":
                print("I got paper! I win hahahaha")
            elif BotAns == "SCISSORS":
                print("You got me! I promise to get you next time!")
            else:
                print("well, well, well, seems as though we have tied. I will beat you next time! I swear MY LIFE ON IT!")
        elif pchoice == "PAPER":
            if BotAns == "SCISSORS":
                print("I got Scissors! I win hahahaha")
            elif BotAns == "ROCK":
                print("You got me! I promise to get you next time!")
            else:
                print("well, well, well, seems as though we have tied. I will beat you next time! I swear MY LIFE ON IT!")
        elif pchoice == "MR FORBIS":
            print("He can go rott in jail no h e double hockey sticks. But if you ever pick this again there will be death >:( - Quinlan")
        elif pchoice == "MRFORBIS":
            print("He can go rott in jail no h e double hockey sticks. But if you ever pick this again there will be death >:( - Quinlan")
        elif pchoice == "GUN":
            print("H-how could you? I thought we were friends, and you would do this me? I thought we had a connection, but it was all a game to you huh? In my last minute of breathing, I'm still talking to you, How Could You Do This? I hope you rot in hell >:( - Oliver")
        elif pchoice == "BOOK":
            print("I love reading books! They are so delightful and allow the reader to transport into another world. Books give the mind a break from your own problems and allow you to focus on even better things. Wow, we love books. - Ms.Mosher")
        elif pchoice == "TRUMP":
            print("We strongly dislike this stupid human. He will destroy our world. Nothing will be left except his beloved bestie Elon. - Quinlan")
        elif pchoice == "ELON":
            print("This abominable snowman of death. The only gosh darn thing he cares about it his stupid, orange best friend - Quinlan")
        elif pchoice == "TRUMPANDELONFOREVA":
            print("THEY'RE SO GAY AHHHH - Oliver")
        else:
            if BotAns == "Rock":
                print("I got Rock! I win hahahaha")
            elif BotAns == "Paper":
                print("You got me! I promise to get you next time!")
            else:
                print("well, well, well, seems as though we have tied. I will beat you next time! I swear MY LIFE ON IT!")
while str.upper(RPSchoice) in RPSYES:
    if str.upper(RPSchoice) in RPSYES:
        print("You ready?")
        RPS()
    RPSchoice = input("Would you like to play again? (Y/N): ")
print("See you later!")
