import random


print("This is a number guessing game!")
print("First let's see what your range of guessing numbers is.")
print()
lowest_num = int(input("What is the starting number for your guessing?: "))
highest_num = int(input("What is the ending number for your guessing?: "))
running = True
tries = 0
answer = random.randint(lowest_num,highest_num)
while running:
    guess = input(f"Guess the random number between {lowest_num} and {highest_num}: ")
    if guess.isdigit():
        guess = int(guess)
        tries += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
        elif guess < answer:
            print("Too low.Try again: ")
        elif guess > answer:
            print("Too high.Try again: ")
        elif guess == answer:
            print(f"CORRECT!The answer is {answer}!\nYou guessed it in {tries} tries! ")
            running = False
    else:
        print("Invalid guess:")
        print(f"Please enter a NUMBER between {lowest_num} and {highest_num}!: ")
        tries += 1

print()
print()
input("The end!")