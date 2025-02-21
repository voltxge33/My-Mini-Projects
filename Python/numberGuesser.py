import random
print("Welcome to my game! In this game, you will be guessing a number of my choice!.\n"
      "Try to pick the right one, because if you don't, there will be consequences.\n"
      "You have 7 guesses, good luck!")
guesses = 7
minimum = input("Pick a number! Any number: ")
is_number = False
while not is_number:
    try:
        minimum = int(minimum)
        is_number = True
    except (ValueError, OverflowError):
        minimum = input("That's not a number! Try again: ")
maximum = input("Now pick a number that is larger than the previous one: ")
is_number2 = False
while not is_number2:
    try:
        maximum = int(maximum)
        is_number2 = True
    except (ValueError, OverflowError):
        maximum = input("That's not a number! Try again: ")


while minimum > maximum:
    if minimum > maximum:
        maximum = input("That's not greater than the previous number!\nPick another number:")

number = random.randint(int(minimum), int(maximum))
print(number)
gues = input("Now choose a number, any number within the range: ")
guess = int(gues)


while guesses != 0:
    try:

        if guesses == 1:
            print("Your out! Try again later!")
            break
        elif guess < int(minimum) or guess > int(maximum):
            guess = input("That's not a number in the range! Don't try to trick me! \nGo again: ")
        elif guess == number:
            print("You got it! Nice job!")
            break
        elif guess != number:
            guesses -= 1
            guess = input("You didn't get it!" + " You have " + str(guesses) + " guesses left" "\n Try again: ")
    except (ValueError, OverflowError):
        guess = input("That's not a number!\nTry again: ")
