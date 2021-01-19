# Python Project Ideas: Beginners Level
# 2. Number Guessing
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

from random import randrange
import random

guess_phrases = ('I thinks it is: ', 'Maybe: ', 'I bet it is: ', 'It is gotta be: ',
                 'I guess it is: ', 'It has to be: ', 'I will go with: ', 'Let it be: ')

repeat = 'y'
yes = 'y'
while repeat == yes.lower():
    print("-------------------------------------------------------")
    gnrtnum = randrange(0, 11)
    lives = 3
    print("It's a number from 0 to 10. Guess it. You have 3 tries.")
    print("-------------------------------------------------------")

    while lives > 0:
        guess = int(input(random.choice(guess_phrases)))
        if guess == gnrtnum:
            print("Congrats! You win!")
            repeat = input("Play again? Y or N: ").lower()
            break
        elif guess > gnrtnum:
            print("Too big, try smaller")
            lives -= 1
            print(f"You have {lives} live(s) left")
            print("------------------------------")
        elif guess < gnrtnum:
            print("Too small, try bigger")
            lives -= 1
            print(f"You have {lives} live(s) left")
            print("------------------------------")
# Repeat sequence
        if lives == 0:
            print("You failed to guess the number")
            repeat = input("Play again? Y or N: ").lower()
