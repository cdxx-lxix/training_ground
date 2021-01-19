# Python Project Ideas: Beginners Level
# 1. Mad Libs Generator
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

import random


print("Sup lad or lass. I will ask you to enter some words.")
print("It can be anything. There are no walls or borders and all the nonsense is accepted.")
print("Let us begin, shall we?")
charname = input("Give me your name: ")
nouns_input = input(
    f"Ok, {charname}. Now write some (no less than 3) NOUNS separated with space: ")
nouns = nouns_input.split()
verbs_input = input(
    "Awesome! Next step, VERBS (no less than 3). Just like nouns, separate them with space: ")
verbs = verbs_input.split()
adjs_input = input(
    "Cool, cool. Last guys on my list - ADJECTIVES. You know what to do: ")
adjs = adjs_input.split()

print("--------------------------------------------------------------------------------------------")

srtStory1 = f'One day {charname} woke up to find himself {random.choice(verbs)} next to {random.choice(nouns)}! What a {random.choice(adjs)} incident.'
srtStory2 = f'{random.choice(nouns)}, {random.choice(nouns)} and {charname} are our most famous {random.choice(nouns)}s. Lets hope they will continue to {random.choice(verbs)} our {random.choice(adjs)} eyes with their sight.'
srtStory3 = f'Lets be honest {charname} tacos are the best in {random.choice(nouns)}-city. Maybe they are {random.choice(adjs)} but it is so {random.choice(adjs)} to {random.choice(verbs)} them!'

storylist = [srtStory1, srtStory2, srtStory3]

print("Hear ye my story!")
print('\n')

repeat = 'y'
yes = 'y'
while repeat.lower() == yes:
    print(random.choice(storylist))
    repeat = input("Want some more? Y | N: ")
    print("--------------------------------------------------------------------------------------------")
