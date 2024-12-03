import random
print("Welcome to my game! In this game, you will be guessing a word of my choice!.\n"
      "Try to pick the right one, because if you don't, there will be consequences.\n"
      "You have 7 guesses, good luck!")
guesses = 7
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print(word)
gues = input("Now choose a word, any word! ")
guess = str.lower(gues)
while guesses != 0:
    if guesses == 1:
        print("Your out! Try again later!")
        break
    elif guess == word:
        print("You got it! Nice job!")
        break
    elif guess != word:
        guesses -= 1
        guess = input("You didn't get it!" + " You have " + str(guesses) + " guesses left" "\n Try again: ")
