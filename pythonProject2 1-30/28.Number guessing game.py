#  PYTHON NUMBER GUESSING GAME

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guess = int(input("Guess the number: "))
tries = 0
while True:
    if guess == answer:
        print(f"CORRECT!")
        tries += 1
        break
    elif guess > highest_num:
        guess = int(input("THAT NUMBER ISN'T IN THE GUESSING RANGE!Guess again: "))
        tries += 1
    elif guess < answer:
        guess = int(input("TOO LOW!Guess again: "))
        tries += 1
    elif guess > answer:
        guess = int(input("TOO HIGH!Guess again: "))
        tries += 1

print(f"You guessed the random number {answer} in {tries} tries!")