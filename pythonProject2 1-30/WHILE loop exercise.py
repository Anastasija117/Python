import random

number = random.randint(1,100)
print("The computer will randomly select a number between 1 and 100.Try to guess the number!")
attempts = 0
while  True:
    guess = int(input("Enter the guessing number: "))
    attempts += 1
    if guess < number:
        print("Too low!Try again.")
    elif guess > 100:
        print("The number needs to be lower than 100!Try again.")
    elif guess > number:
        print("Too high!Try again.")
    elif guess == number:
        print(f"Correct!You guessed the number in {attempts} attempts!")
        break
input("The end")