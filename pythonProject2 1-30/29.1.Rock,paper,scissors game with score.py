# ROCK PAPER SCISSORS GAME
import random

options = ("rock","paper","scissors")

running = True
player_score = 0
computer_score = 0
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win this round!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win this round!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win this round!")
        player_score += 1
    else:
        print("You lose this round!")
        computer_score += 1

    if not input("Play again?(y/n): ").lower() == "y":
        running = False

if player_score > computer_score:
    print(f"Your score: {player_score},computer score: {computer_score}")
    print("You won the game!Congratulations!")
elif computer_score > player_score:
    print(f"Your score: {player_score}, computer score: {computer_score}")
    print("You lost the game!Better luck next time!")
else:
    print(f"Your score: {player_score},computer score: {computer_score}")
    print("It's a tie!")
input("Thanks for playing!")





