# Python Project Ideas: Beginners Level
# 5. Hangman
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

import getpass

print("Welcome to the hangman mini game!")
print("Rules are simple:")
print("1. Enter your word and the second player have to guess it letter by letter")
print("2. The one who guesses got 5 mistakes to spare")
print("3. Type whole word to complete even if you guessed all of the letters")
print("Lets begin")
print("--------------------------------------------------------------------------")

repeat = 'y'
yes = 'y'
while repeat.lower() == yes:
    def dashReplace(secret, dash, rq_guess):
        result = ""
        for i in range(len(secret)):
            if secret[i] == rq_guess:
                result = result + rq_guess
            else:
                result = result + dash[i]

        return result

    word = getpass.getpass("Enter your word: ").lower()
    dashes = "-" * len(word)
    print("Accepted")
    print("Now it is time for the second player to take control")
    print(f"The word consists of {len(word)} letters")
    print(f"::: {dashes} :::")
    guess = input("Your guess (just one letter or whole word): ").lower()

    lives = 5
    while lives > 0:
        if guess.lower() == word.lower():
            print(f"Congratz! You guessed right the whole word - {word}")
            break
        elif guess.lower() in word.lower():
            print(f"Yes {guess} is there")
            dashes = dashReplace(word, dashes, guess)
            print(f"::: {dashes} :::")
            guess = input(
                "Your next guess (just one letter or whole word): ").lower()
        else:
            lives -= 1
            print(f"Wrong. You have {lives} mistakes left")
            print(f"::: {dashes} :::")
            guess = input(
                "Your next guess (just one letter or whole word): ").lower()
        if lives == 0:
            print(f"You failed to guess the word. It was {word}")
            break
    repeat = input("Play again? Y | N : ")
